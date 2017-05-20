set build_name=%1%
rem Remove the trailing slash
if %build_name:~-1%==\ set build_name=%build_name:~0,-1%
rem Package contents into a zip file
python ..\zip.py %build_name%.zip %build_name%\WindowsNoEditor
rem Upload binary
python ..\gdrive_upload.py %build_name%.zip
