# unrealcv-packaging

The task of this repository is defined as json files. See the schema file for the json in `task.schema`, see an example in `playground_UE414.json`. Run `python validate_task.py [Name].json` to see whether the json is in a correct format.

Packaging scripts for UnrealCV

## Scripts

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


## Prepare

1. Download and put uproject into `uproject` folder. Packaged binaries will be saved to the `uproject` folder.

2. Clone UnrealCV

`git clone https://github.com/unrealcv/unrealcv.git`


## Linux

1. Compile UnrealEngine from source code

  `git clone -b 4.14 https://github.com/EpicGames/UnrealEngine.git`

  `sh linux/docker/build-ue4.sh`

2. Build UnrealCV

  `sh linux/docker/build-unrealcv.sh`

3. Package uproject (make sure update the UnrealCV version)

  `sh linux/docker/package.sh repos/[ProjectFolder]/[ProjectName].uproject`

### Packaging Docker Image

Docker image of RealisticRendering is provided, but `nvidia-docker` is only supported in Linux.

Package docker image. Run this to build the newest image and also push the image to Dockerhub.

`sh linux/docker/build-rr-image.sh`

## Mac

1. Build UnrealCV

  `sh mac/build-unrealcv.sh`

2. Package uproject

  `sh mac/package.sh repos/[ProjectFolder]/[ProjectName].uproject`

## Windows

1. Build UnrealCV

  `sh windows/build-unrealcv.sh`

2. Package uproject

  `sh mac/package.sh repos/[ProjectFolder]/[ProjectName].uproject`


## Run test for checking binaries

Run `setup.sh` in `model-zoo-test` to download the binary.

I can use a base docker image to run the binary, which is easier to control.

Make sure I have a copy of unrealcv code I can use.

A few things to check.

0. Whether it crashes? Whether it can connect successfully?
-. Whether the object mask is clearly generated.
-. Whether the object mask aligns well with the image.
-. Whether all materials are correctly displayed?
