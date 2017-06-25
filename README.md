# unrealcv-packaging
Packing scripts for unrealcv

Run the test of unrealcv first before packaging!

Required scripts
1. build-unrealcv - Build UnrealCV plugin binary
2. package - Install plugin and create a game binary

- linux/                # Packaging scripts for linux

    - docker/

        - build-ue4.sh      # Linux requires the compilation of UE4 from code
        - build-rr-image.sh
        - build-unrealcv.sh
        - package.sh
        - run-editor.sh

- windows/              # Packaging scripts for windows

    - build-unrealcv.bat
    - package.bat

- mac/                  # Packaging scripts for mac, might be redundant as the linux version

    - build-unrealcv.sh
    - package.sh

- common/               # Functions shared

    - build-conf.py       # Get the plugin configuration information

- repos/                # Clone Unreal projects to local disk

- test/                 # Script to download a binary for testing.

- docs/                 # Documentation for this repository

## Linux

The important part is testing the binary and make sure it work properly. This is done by the scripts in the `model-zoo-test` folder, which is platform independent.

Run `../model-zoo-test/run-test.sh` to verify the correctness of binaries.

## Windows


## Run test for checking binaries

Run `setup.sh` in `model-zoo-test` to download the binary.

I can use a base docker image to run the binary, which is easier to control.

Make sure I have a copy of unrealcv code I can use.

A few things to check.

0. Whether it crashes? Whether it can connect successfully?
-. Whether the object mask is clearly generated.
-. Whether the object mask aligns well with the image.
-. Whether all materials are correctly displayed?


## Docker packaging

Run `build.sh` to build the newest image and also push the image to dockerhub.
