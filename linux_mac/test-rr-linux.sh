./RealisticRendering-Linux-0.3.8/LinuxNoEditor/RealisticRendering/Binaries/Linux/RealisticRendering &
pid=$!
sleep 2

pytest unrealcv/test/rr_test.py
kill ${pid}
