# Download the latelest version of RR binary.
export version=$(python ../common/build-conf.py --format "{unrealcv_version}")

# Parse the filename to get the version of the UnrealCV version.
# version=$(echo ${url} | sed 's/.*\/Linux-\(.*\).zip/\1/')
echo ${version}

# # Pull the basic nvidia docker image.
docker pull qiuwch/nvidia

rr_folder=RealisticRendering-Linux-${version}
cp Dockerfile ${rr_folder}
# Do the build in the rr_folder to avoid the very large context files

# Run and commit the docker image
docker build --build-arg unrealcv_version=${version} ${rr_folder} -t qiuwch/rr:${version}

# Push this docker image to the dockerhub.
docker push qiuwch/rr:${version}
