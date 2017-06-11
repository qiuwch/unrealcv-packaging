# Run some test of RR to make sure everything works well. Make sure no warning and error
# Only do this with RR, because we know a lot about this environment
open RealisticRendering-Darwin-0.3.8/MacNoEditor/RealisticRendering.app
sleep 2

pytest unrealcv/test/connection_test.py
pytest unrealcv/test/camera_test.py
pytest unrealcv/test/object_test.py
pytest unrealcv/test/stereo_test.py
pytest unrealcv/test/rr_test.py

pkill RealisticRendering
