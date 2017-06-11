#!/bin/bash
project=$1 # set can only be used for windows batch command 
echo ${project}
project_folder=$(dirname ${project})
plugin_binary=unrealcv/Plugins 

if [ ! -d ${plugin_binary} ]; then
    sh build-unrealcv.sh
fi

# project_folder=$1
if [ -z ${project_folder} ]; then
    echo Please specify project folder, can not be empty
    exit
fi 

echo Project folder is ${project_folder}
rm -rf ${project_folder}/Plugins/UnrealCV
cp -r ${plugin_binary} ${project_folder}
