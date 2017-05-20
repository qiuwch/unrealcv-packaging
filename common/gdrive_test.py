from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file2 = drive.CreateFile()
file2.SetContentFile('README.md')
file2.Upload()
