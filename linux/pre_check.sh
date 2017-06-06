config=UnrealEngine/Engine/Config/ConsoleVariables.ini

if grep -Fq "r.ForceDebugViewModes = 1" ${config}; then
    echo "Debug flag has been enabled."
else
    echo "Error: debug flag is not properly set."
fi

