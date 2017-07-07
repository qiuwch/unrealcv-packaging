from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()
    filename = args.file

    gauth = GoogleAuth()
    # gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file2 = drive.CreateFile()
    file2.SetContentFile(filename)
    file2.Upload()
