'''
TODO: Check UE4 Version
TODO: Check UnrealCV version
'''
import argparse, json, os, sys, logging, subprocess, time, signal

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

class Timer:
    ''' Record execution time '''
    def __enter__(self):
        self.tic = time.time()

    def __exit__(self, type, val, tb):
        self.toc = time.time()
        self.elapse = self.toc - self.tic

    def GetElapsed(self):
        return self.elapse

class TaskRunner:
    def __init__(self, opt):
        self.opt = opt
        self.env = dict()

    def _setup_environ(self): # private
        def opt(*args):
            path = 'opt' + ''.join(["['%s']" % v for v in args])
            value = self.opt
            for key in args:
                if value:
                    value = value.get(key)
            if value is None:
                print('Warning: value of %s can not be found' % path)
                return None
            return value

        ''' Setup os environment variables based on the config '''
        logger.info('Setup os environment variables')

        mapping = dict(
            TaskName = self.opt['TaskName'], # Required
        )

        self.env = dict(
            TaskName = opt('TaskName'), # Required
            UE4 = opt('UE4', 'Path'),
            UnrealCV = opt('UnrealCV', 'Path'),
            UProject = opt('UProject', 'Path'),
            UnrealCV_Version = opt('UnrealCV', 'Version'),
            UE4_Version = opt('UE4', 'Version'),
            OS_Name = opt('OS'),
            HOME = os.environ['HOME'],
            PWD = os.getcwd()
        )

        # Optional args
        # Write in this way is more flexible than defining a function
        # if self.opt.get('UE4'):
        #     # mapping['UE4'] = self.opt['UE4']['Path'] # Required
        #     mapping['UE4']
        #
        # if self.opt.get('UnrealCV'):
        #     mapping['UnrealCV'] = self.opt['UnrealCV']['Path'] # Optinal
        #
        # if self.opt.get('UProject'):
        #     mapping['UProject'] = self.opt['UProject']['Path'] # Optional

        # for (k,v) in mapping.iteritems():
        #     # Windows can not distinguish upper-lower cases
        #     # Windows can only use upper-case os environment variables
        #     self.env[k] = v

        # Update os.environ
        # for (k,v) in self.env.iteritems():
        #     os.environ[k] = v
        for k in ['UE4', 'UnrealCV']:
            if self.env.get(k):
                os.environ[k] = self.env[k]


        # self.env['HOME'] = os.environ['HOME']
        # self.env['PWD'] = os.getcwd() # For cross-platform support

        # Populate some special variables

        # Expand self.opt with self.env
        def _update_opt(node):
            if isinstance(node, dict):
                for (k, v) in node.iteritems():
                    if isinstance(v, basestring):
                        node[k] = v.format(**self.env)
                        logger.debug('Update key %s to %s' % (k, node[k]))
                    _update_opt(v)

            if isinstance(node, list):
                for i in range(len(node)):
                    v = node[i]
                    _update_opt(v)
                    if isinstance(v, basestring):
                        node[i] = v.format(**self.env)
                        logger.debug('Update %s' % (node[i]))


        logger.info("Update opt with self.env")
        _update_opt(self.opt)
        self._setup_check()

    def _setup_check(self):
        def _verbose_assert(expect, value):
            assert expect == value, 'Expect %s, but get %s' % (str(expect), str(value))

        sys.path.append('./common')
        import build_conf
        # Check whether the configuration is valid
        # Check UE4, check UE4 version

        # Check UnrealCV, check UnrealCV version

        env_data = dict(
            OS = build_conf.parse_platform(),
            UE4_version = build_conf.parse_ue4_version(),
            UnrealCV_version = build_conf.parse_unrealcv_version()
        )

        # Check whether the task setting is the same as the running environment
        if self.opt.get('UnrealCV'):
            _verbose_assert(self.opt.get('UnrealCV').get('Version'), env_data.get('UnrealCV_version'))

        if self.opt.get('UE4'):
            _verbose_assert(self.opt.get('UE4').get('Version'), env_data.get('UE4_version'))

        _verbose_assert(self.opt.get('OS'), env_data.get('OS'))

        # Check uproject
        if self.env.get('UProject'):
            pass

    def run(self):
        self._setup_environ()

        report_filename = self.opt['Report']
        self.report = open(report_filename, 'w')

        for script in self.opt['Scripts']:
            self._run_script(script)

        self.report.close()

    def _run_script(self, script):
        ''' Run a defined script '''
        # Pick 'task' instead of 'run', because 'run' can also be a verb.
        logger.info('Script to run %s' % script)
        logger.info('Script to run %s' % ' '.join(script['Path']))

        # Required fields
        script_path = script['Path']
        # Optional fields
        use_cache = script.get('Cache')
        cwd = script.get('CWD') # optional
        log_filename = script.get('Log')

        if use_cache is None: # Not defined
            # By default this is true
            use_cache = True

        if use_cache and log_filename and os.path.isfile(log_filename):
            logger.info('Log file %s exists, skip this script' % log_filename)
            return

        if log_filename:
            log_file = open(log_filename, 'w')
        else:
            log_file = None

        # subprocess.call(script, env=os.environ) # Run with an updated system environment
        timer = Timer()
        with timer:
            global popen_obj
            popen_obj = subprocess.Popen(script_path, cwd = cwd, stdout = subprocess.PIPE)
            # popen_obj = subprocess.Popen(script, cwd = cwd)

            # [stdoutdata, stderrdata] = popen_obj.communicate()
            while popen_obj.poll() is None:
                l = popen_obj.stdout.readline()
                # import ipdb; ipdb.set_trace()
                if log_file:
                    line = l.replace(r"\r\n", r"\n") # Make it consistent
                    log_file.write(line)
                    # log_file.write('A line break\n')
                logger.info(l.strip())

        if self.report:
            self.report.write('Run script %s \n' % script)
            self.report.write('Time: %.2f sec \n' % timer.GetElapsed())
            self.report.write('Exit code: %d \n' % popen_obj.returncode)

popen_obj = None

def engine_check():
    # config=UnrealEngine/Engine/Config/ConsoleVariables.ini
    # if grep -Fq "r.ForceDebugViewModes = 1" ${config}; then
    pass

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    if popen_obj:
        popen_obj.kill()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', help='Config file to run the test', default='template.json')

    args = parser.parse_args()

    config = json.load(open(args.config))
    # print(config)
    runner = TaskRunner(config['Tasks'][0])
    runner.run()


if __name__ == '__main__':
    main()
