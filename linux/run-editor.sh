nvidia-docker run -it --rm --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency /UE4/Engine/Binaries/Linux/UE4Editor
