./RealisticRendering-Linux-0.3.8/LinuxNoEditor/RealisticRendering/Binaries/Linux/RealisticRendering > rr.log  &
pid=$!
sleep 2

pytest unrealcv/test/connection_test.py
pytest unrealcv/test/camera_test.py
pytest unrealcv/test/object_test.py
pytest unrealcv/test/stereo_test.py
pytest unrealcv/test/rr_test.py
kill ${pid}
