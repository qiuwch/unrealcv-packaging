call config.bat
set project=%1%
if not exist %project% (
	rem File not exist
	goto:eof
)

set cmd="%UE4%\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%project% -archivedirectory=%CD%/built -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -allmaps -stage -pak -archive -cook
if exist %project%/Source (
	rem Build source code 
    cmd=%cmd% -build
) 
%cmd%
