set project=%~f1
set output_folder=%~f2
rem Available options in here http://stackoverflow.com/questions/659647/how-to-get-folder-path-from-file-path-with-cmd
set project_folder=%~dp1
set project_name=%~n1

REM for /f "delims=" %%i in ('command') do set output=%%i
python %~dp0\..\common\build-conf.py --format {platform}-{unrealcv_version} > build-conf.txt
set /p build_suffix=<build-conf.txt
set build_name=%project_name%-%build_suffix%
set output_folder=%output_folder%\%build_name%

if not exist %project% (
	rem File not exist
	goto:eof
)

REM "%UE4%"\Engine\Build\BatchFiles\Build.bat %project_name%Editor Win64 Development %project% -waitmutex

set cmd="%UE4%\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%project% -archivedirectory=%output_folder% -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -allmaps -stage -pak -archive -cook -build
REM if exist %project_folder%\Source (
REM 	rem Build source code
REM     set cmd=%cmd% -build
REM )
%cmd%

REM call release.bat %build_name%
