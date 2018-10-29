## How to package for windows

- Change the engine configuration file according to here

http://docs.unrealcv.org/en/develop/plugin/package.html#modify-an-ue4-config-file 

- Clone repositories into `../repos`

`sh clone.sh`

- Clone `unrealcv`

`git clone https://github.com/unrealcv/unrealcv.git -b develop`

- Build `unrealcv`

`build-plugin.bat`

<!-- - Install plugin to project? -->

- Package a binary
