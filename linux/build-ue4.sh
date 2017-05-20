docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 unrealcv/ue4-dependency bash -c "sudo chown -R unrealcv /UE4; cd UE4; sudo apt-get update; ./Setup.sh; ./GenerateProjectFiles.sh; make -C /UE4"
