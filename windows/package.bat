call config.bat
set project=%1%
rem Available options in here http://stackoverflow.com/questions/659647/how-to-get-folder-path-from-file-path-with-cmd
set project_folder=%~dp1%
set project_name=%~n1%

python ..\common\build-conf.py --format {platform}_{unrealcv_version} > build-conf.txt
set /p build_suffix=<build-conf.txt
set build_name=%project_name%-%build_suffix%
set output_folder=%CD%\%build_name%

if not exist %project% (
	rem File not exist
	goto:eof
)

set cmd="%UE4%\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%project% -archivedirectory=%output_folder% -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -allmaps -stage -pak -archive -cook -build
if exist %project_folder%\Source (
	rem Build source code 
    set cmd=%cmd% -build
) 
%cmd%

call release.bat %build_name%
