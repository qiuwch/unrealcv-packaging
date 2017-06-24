import os, zipfile, subprocess, time
import pytest

# Run test in windows
class UrlParser(object):
    def __init__(self, url):
        self.basename = os.path.basename(url)

# The environment runner
class Binary(object):
    ''' Base class for binary '''
    def __init__(self, url):
        self.url = url
        url_parser = UrlParser(url)
        self.basename = url_parser.basename
        self.unzip_folder = self.basename.replace('.zip', '')
        self.project_name = self.basename.split('-')[0]

    def download(self):
        # Download the file
        if not os.path.isfile(self.basename):
            print('Zip file %s not exist, please download it from %s' % (self.basename, self.url))
            sys.exit(-1)

        # Unzip file
        if not os.path.isdir(self.unzip_folder):
            print('Unzip file %s' % self.basename)
            zip_ref = zipfile.ZipFile(self.basename, 'r')
            zip_ref.extractall(self.unzip_folder)
            zip_ref.close()
        else:
            print('Folder %s exist, skip unzip' % self.unzip_folder)

    def __enter__(self):
        ''' Start the binary '''
        # Download the binary if not exist
        self.download()
        self.start()

    def __exit__(self, type, value, traceback):
        ''' Close the binary '''
        self.close()

class WinBinary(Binary):
    def start(self):
        self.exe = self.project_name + '.exe'
        self.win_binary = os.path.join(self.unzip_folder, self.exe)
        print('Start windows binary %s' % self.win_binary)
        # subprocess.call(self.win_binary)
        subprocess.Popen(self.win_binary)
        time.sleep(10)

    def close(self):
        # Kill windows process
        # See this https://github.com/qiuwch/unrealcv-packaging/blob/master/windows/test-rr.bat
        cmd = ['taskkill', '/F', '/IM', self.exe]
        print('Kill windows binary with command %s' % cmd)
        subprocess.call(cmd)

class LinuxBinary(Binary):
    def start(self):
        pass

    def close(self):
        pass


def test_url(url, test_scripts):
    # parser = UrlParser(url)
    # print(parser.basename)
    # print('Basename: ', basename)
    binary = WinBinary(url)

    with binary:
        print('Run test script')
        pytest.main(test_scripts)

if __name__ == '__main__':
    root_url = 'http://cs.jhu.edu/~qiuwch/release/unrealcv/'
    urls = [
        'RealisticRendering-Windows-0.3.9.zip',
        'ArchinteriorsVol2Scene1-Windows-0.3.6.zip',
        'ArchinteriorsVol2Scene2-Windows-0.3.6.zip',
        'ArchinteriorsVol2Scene3-Windows-0.3.6.zip',
        'UrbanCity-Windows-0.3.6.zip',
    ]
    urls = [root_url + v for v in urls]

    test_scripts = [
        'connection_test.py',
        'camera_test.py',
        'stereo_test.py',
        'object_test.py',
    ]
    test_scripts = ['unrealcv/test/' + v for v in test_scripts]
    for script in test_scripts:
        if not os.path.isfile(script):
            print('Test script %s, not exist.' % script)
            sys.exit(-1)

    for url in urls:
        test_url(url, test_scripts)
