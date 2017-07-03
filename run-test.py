import argparse, json, os, sys, logging, subprocess, time

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
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

class Tee(object):
    ''' Output to both stdout and a file
    from: https://stackoverflow.com/questions/616645/how-do-i-duplicate-sys-stdout-to-a-log-file-in-python
    '''
    def __init__(self, name, mode):
        self.file = open(name, mode)
        self.stdout = sys.stdout
        # sys.stdout = self
        self.fileno = sys.stdout.fileno

    def __del__(self):
        self.file.close()

    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)

class TaskRunner:
    def __init__(self, opt):
        self.opt = opt
        self.env = dict()

    def setup_environ(self):
        ''' Setup os environment variables based on the config '''
        logger.info('Setup os environment variables')

        mapping = dict(
            UE4 = self.opt['UE4']['Path'],
            UnrealCV = self.opt['UnrealCV']['Path'],
            TaskName = self.opt['TaskName']
        )

        for (k,v) in mapping.iteritems():
            os.environ[k] = v
            # Windows can not distinguish upper-lower cases
            # Windows can only use upper-case os environment variables
            self.env[k] = v

        self.env['HOME'] = os.environ['HOME']
        self.env['PWD'] = os.getcwd() # For cross-platform support

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


    def run(self):
        self.setup_environ()

        report_filename = self.opt['Report']
        report = open(report_filename, 'w')

        for script in self.opt['Scripts']:
            # Pick 'task' instead of 'run', because 'run' can also be a verb.
            script_path = script['Path']
            # Format the script in a cross-platform way

            cwd = script.get('CWD') # optional

            log_filename = script.get('Log')
            log_file = open(log_filename, 'w')

            logger.info('Script to run %s' % script)
            # subprocess.call(script, env=os.environ) # Run with an updated system environment
            timer = Timer()
            report.write('Run script %s \n' % script)
            with timer:
                popen_obj = subprocess.Popen(script_path, cwd = cwd, stdout = subprocess.PIPE)
                # popen_obj = subprocess.Popen(script, cwd = cwd)

            # [stdoutdata, stderrdata] = popen_obj.communicate()
            while popen_obj.poll() is None:
                l = popen_obj.stdout.readline()
                if log_file: log_file.write(l)
                logger.info(l.strip())

            report.write('Time: %.2f sec \n' % timer.GetElapsed())
            report.write('Exit code: %d \n' % popen_obj.returncode)


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
