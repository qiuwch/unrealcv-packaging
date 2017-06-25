version=$(python ../common/build-conf.py --format "{unrealcv_version}")
nvidia-docker run --rm -p 9000:9000 --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    qiuwch/rr:${version} > log/docker-rr.log &

pid=$!
sleep 2
#
pytest unrealcv/test/connection_test.py
pytest unrealcv/test/camera_test.py
pytest unrealcv/test/object_test.py
pytest unrealcv/test/stereo_test.py
pytest unrealcv/test/rr_test.py

kill ${pid}
