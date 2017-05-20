Generic setting
===============

`Git lfs` needs to be installed first!!
`git lfs` seems having some issues with cmder.

Linux
=====

The Linux version is roughly identical to windows version, the difference is the Linux version uses docker as its executable.

Prepare Unreal Engine binaries, build the docker image
------------------------------------------------------

.. code::

    cd ~/workspace
    git clone https://github.com/qiuwch/unrealcv-docker-images
    cd unrealcv-docker-images
    make ue4-base
     
- Make an Unreal Engine image or pull from the docker hub, Compile the engine code, because it is version dependent

.. code::
  
  # Clone the Unreal Engine repository which will take a few minutes
  git clone -b 4.14 https://github.com/EpicGames/UnrealEngine.git
  # Compile the engine code
  sh build-ue4.sh
  

Install the windows machine
===========================

- Download Unreal Engine and install it
- Install cmder and extract it.
- How to change the UE4 environment variable?
- Disable ctrl-w for cmder, so that I can use vim correctly.

.. code::

  cd windows
  git clone https://github.com/unrealcv/unrealcv

.. code::

  build-plugin.bat
  install-plugin.bat [project.uproject]
  # Package project
  package.bat [project.uproject]  
  
 
