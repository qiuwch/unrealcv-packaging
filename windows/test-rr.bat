REM Run some test of RR to make sure everything works well. Make sure no warning and error
REM Only do this with RR, because we know a lot about this environment

REM Start it first
REM Make sure not waiting for the exit of this.
REM call .\RealisticRendering-Windows-0.3.8\WindowsNoEditor\RealisticRendering.exe
start .\RealisticRendering-Windows-0.3.8\WindowsNoEditor\RealisticRendering.exe
sleep 2
REM give some time for it to populate.

REM TODO: Replace all these with pytest unrealcv/test
pytest unrealcv/test/connection_test.py
REM pytest unrealcv/test/camera_test.py
REM pytest unrealcv/test/object_test.py
REM pytest unrealcv/test/stereo_test.py
pytest unrealcv/test/rr_test.py

REM Is there an automatic way to kill the running UE4 app?
taskkill /F /IM RealisticRendering.exe
