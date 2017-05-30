scene_name=$(basename $1)
unrealcv_root=./unrealcv
if [ -z ${scene_name} ]; then
  echo scene_name can not be empty
  exit
fi

cmd=${scene_name}/${scene_name}/Binaries/Linux/${scene_name}
echo ${cmd}
${cmd} > /dev/null &
pid=$!

# Run some test
echo Run some test
sleep 2 
pytest unrealcv/test/connection_test.py

kill ${pid}
