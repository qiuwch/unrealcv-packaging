if [ ! -d ./UnrealEngine ]
then
    echo "Use git clone to download UnrealEngine source code first."
fi
docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 qiuwch/ue4-base bash -c "sudo chown -R unrealcv /UE4; cd UE4; sudo apt-get update; ./Setup.sh; ./GenerateProjectFiles.sh; make -C /UE4"
