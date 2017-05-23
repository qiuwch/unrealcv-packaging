docker run -it --rm \
    -v ${PWD}/unrealcv:/unrealcv \
    -v ${PWD}/UnrealEngine:/UE4 \
    -e UE4=/UE4 \
    qiuwch/ue4-base \
    /bin/sh -c "sudo chown -R unrealcv /unrealcv; cd /unrealcv; sh ./build.sh"
