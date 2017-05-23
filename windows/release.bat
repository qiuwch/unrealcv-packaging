set build_name=%1%
rem Remove the trailing slash
if %build_name:~-1%==\ set build_name=%build_name:~0,-1%
rem Package contents into a zip file
python ..\common\zip.py %build_name%.zip %build_name%\WindowsNoEditor
rem Upload binary
rem python ..\common\gdrive_upload.py %build_name%.zip
scp %build_name%.zip qiuwch@gradx.cs.jhu.edu:/users/qiuwch/public_html/release/unrealcv/
