import os, zipfile, subprocess, time, sys, argparse, platform
import pytest

# Run test in windows
# class UrlParser(object):
#     def __init__(self, url):
#         self.basename = os.path.basename(url)

# The environment runner
class Binary(object):
    ''' Base class for binary '''
    def __init__(self, binary_path):
        self.binary_path = binary_path
        # self.url = url
        # url_parser = UrlParser(url)
        # self.basename = url_parser.basename
        # self.unzip_folder = self.basename.replace('.zip', '')
        # self.project_name = self.basename.split('-')[0]

    # def download(self):
    #     # Download the file
    #     if not os.path.isfile(self.basename):
    #         print('Zip file %s not exist, please download it from %s' % (self.basename, self.url))
    #         sys.exit(-1)
    #
    #     # Unzip file
    #     if not os.path.isdir(self.unzip_folder):
    #         print('Unzip file %s' % self.basename)
    #         zip_ref = zipfile.ZipFile(self.basename, 'r')
    #         zip_ref.extractall(self.unzip_folder)
    #         zip_ref.close()
    #     else:
    #         print('Folder %s exist, skip unzip' % self.unzip_folder)

    def __enter__(self):
        ''' Start the binary '''
        # Download the binary if not exist
        # self.download()
        if os.path.isfile(self.binary_path) or os.path.isdir(self.binary_path):
            self.start()
        else:
            print('Binary %s can not be found' % self.binary_path)
            sys.exit(-1)


    def __exit__(self, type, value, traceback):
        ''' Close the binary '''
        self.close()

class WindowsBinary(Binary):
    def start(self):
        # self.exe = self.project_name + '.exe'
        # self.win_binary = os.path.join(self.unzip_folder, self.exe)
        print('Start windows binary %s' % self.binary_path)
        # subprocess.call(self.win_binary)
        subprocess.Popen(self.binary_path)
        time.sleep(10)
        # Wait for the process to run. FIXME: Wait for an output line?

    def close(self):
        # Kill windows process
        # See this https://github.com/qiuwch/unrealcv-packaging/blob/master/windows/test-rr.bat
        basename = os.path.basename(self.binary_path)
        cmd = ['taskkill', '/F', '/IM', basename]
        print('Kill windows binary with command %s' % cmd)
        subprocess.call(cmd)

class LinuxBinary(Binary):
    '''
    TODO: Can this support mac?
    '''
    def start(self):
        # self.linux_binary = os.path.join(self.unzip_folder, self.project_name, self.project_name,
            # 'Binaries', 'Linux', self.project_name)

        null_file = open(os.devnull, 'w')
        popen_obj = subprocess.Popen([self.binary_path], stdout = null_file, stderr = null_file)
        self.pid = popen_obj.pid
        time.sleep(6)

    def close(self):
        # Kill Linux process
        cmd = ['kill', str(self.pid)]
        print('Kill process %s with command %s' % (self.pid, cmd))
        subprocess.call(cmd)

class MacBinary(Binary):
    def start(self):
        popen_obj = subprocess.Popen([
            'open',
            self.binary_path
        ])
        self.program_name = os.path.basename(self.binary_path).replace('.app', '')
        # TODO: Track the stdout to see whether it is started?
        time.sleep(5)

    def close(self):
        subprocess.call(['pkill', self.program_name])

class DockerBinary(Binary):
    def start(self):
        # nvidia-docker run --rm -p 9000:9000 --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" qiuwch/rr:${version} > log/docker-rr.log &
        pass

    def close(self):
        pass

# For MAC:
# open RealisticRendering-Darwin-0.3.8/MacNoEditor/RealisticRendering.app
# pkill RealisticRendering

def run_test(binary_path, test_scripts):
    # parser = UrlParser(url)
    # print(parser.basename)
    # print('Basename: ', basename)
    # binary = WinBinary(url)
    system_name = platform.system()
    if system_name == 'Windows':
        binary = WindowsBinary(binary_path)
    elif system_name == 'Linux':
        binary = LinuxBinary(binary_path)
    elif system_name == 'Darwin':
        binary = MacBinary(binary_path)

    with binary:
        print('Run test script')
        pytest.main(test_scripts)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', help='The binary to run', required=True)

    args = parser.parse_args()

    test_scripts = [
        'connection_test.py',
        'camera_test.py',
        'stereo_test.py',
        'object_test.py',
    ]
    test_scripts = [os.path.join(os.environ['UnrealCV'], 'test', v) for v in test_scripts]
    for script in test_scripts:
        if not os.path.isfile(script):
            print('Test script %s, not exist.' % script)
            sys.exit(-1)

    run_test(args.binary, test_scripts)
