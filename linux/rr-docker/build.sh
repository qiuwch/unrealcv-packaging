# Download the latelest version of RR binary.
version=0.3.6
url=http://cs.jhu.edu/~qiuwch/release/unrealcv/RealisticRendering-Linux-${version}.zip
wget -c ${url}

# Parse the filename to get the version of the UnrealCV version.
# version=$(echo ${url} | sed 's/.*\/Linux-\(.*\).zip/\1/')
echo ${version}

# # Pull the basic nvidia docker image.
# docker pull qiuwch/nvidia

# Run and commit the docker image
docker build . -t qiuwch/rr:${version}

# Push this docker image to the dockerhub.
docker push qiuwch/rr:${version}
