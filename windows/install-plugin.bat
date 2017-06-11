set plugin_binary=unrealcv\Plugins
set project=%1%
set project_folder=%~dp1%
if "%project%"=="" (
    rem Project file can not be empty
    goto blank
)

rem %project_folder%

if not exist %plugin_binary% (
    rem Build plugin first
    call build-plugin.bat
)

xcopy /e /y /q %plugin_binary% %project_folder%\Plugins\
