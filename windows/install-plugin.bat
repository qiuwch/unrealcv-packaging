set project=%1%
set plugin_binary=%2%
set project_folder=%~dp1
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
