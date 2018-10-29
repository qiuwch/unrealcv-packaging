# Use sh -x package.sh to debug this script
# source config.sh
project=$(readlink -f $1)
project_folder=$(dirname ${project})
project_name=$(basename ${project} .uproject)

export UE4=./UnrealEngine/
build_suffix=$(python ../common/build-conf.py --format "{platform}-{unrealcv_version}")
build_name=${project_name}-${build_suffix}

output_folder=${PWD}/${build_name}

# File existence tests
if [ ! -f ${project} ]; then
    echo File not exist; exit
fi

config=Development
cmd="/UE4/Engine/Build/BatchFiles/RunUAT.sh BuildCookRun \
    -project=/project/${project_name}.uproject -archivedirectory=/output \
    -noP4 -platform=Linux -clientconfig=${config} -serverconfig=${config} -allmaps -stage -pak -archive -cook -build"
echo ${cmd}

# build is also required for Linux
# if [ -d ${project_folder}/Source ]; then
#     echo Build c++ code also
#     cmd=${cmd} "-build"
# fi
# docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 qiuwch/ue4-base bash -c "sudo chown -R unrealcv /UE4; cd UE4; sudo apt-get update; ./Setup.sh; ./GenerateProjectFiles.sh; make -C /UE4"
docker run -it --rm -v ${PWD}/UnrealEngine:/UE4 \
    -v ${project_folder}:/project \
    -v ${output_folder}:/output \
    qiuwch/ue4-base bash -c "sudo chown -R unrealcv /output /project; ${cmd}" \
    | tee ${build_name}.log

if [ $? -eq 0 ]; then
    echo 'Successfully build the binary'
    # sh release.sh ${build_name}
else
    echo "Fail to package the binary"
fi
