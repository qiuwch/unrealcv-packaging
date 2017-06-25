build_name=$(basename $1)
scene_name=$(echo ${build_name} | sed 's/\(.*\)-Linux.*/\1/')
unrealcv_root=./unrealcv
if [ -z ${scene_name} ]; then
  echo scene_name can not be empty
  exit
fi

cmd=${build_name}/LinuxNoEditor/${scene_name}/Binaries/Linux/${scene_name}
echo ${cmd}
${cmd} > ${build_name}.log &
pid=$!

# Run some test
echo Run some test
sleep 2
pytest unrealcv/test/connection_test.py
pytest unrealcv/test/camera_test.py

kill ${pid}
