# Use sh -x package.sh to debug this script
# source config.sh
platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
   platform='Linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
   platform='Mac'
fi

project=$(greadlink -f $1)
project_folder=$(dirname ${project})
project_name=$(basename ${project} .uproject)

build_suffix=$(python ../common/build-conf.py --format "{platform}-{unrealcv_version}")
build_name=${project_name}-${build_suffix}
output_folder=${PWD}/${build_name}

# File existence tests
if [ ! -f ${project} ]; then
    echo File not exist; exit
fi

UE4="/Users/Shared/Epic Games/UE_4.14/"

config=Development
# config=DebugGame # This is one option.
"${UE4}"/Engine/Build/BatchFiles/RunUAT.sh BuildCookRun \
    -project=${project} -archivedirectory=${output_folder} \
    -noP4 -platform=${platform} -clientconfig=${config} -serverconfig=${config} \
    -allmaps -stage -pak -archive -cook -build

if [ $? -eq 0 ]; then
    echo "Build is successful"
    # sh release.sh ${build_name}
else
    echo "Fail to package the binary"
fi
