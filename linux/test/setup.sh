# All all binaries need to be tested.
url=$1
name=$(echo ${url} | sed 's/.*\/\(.*\)-Linux.*/\1/')
zip_file=$(echo ${url} | sed 's/.*\/\(.*-Linux.*zip\)/\1/')
echo ${name}
mkdir ${name}
cd ${name}
wget -c ${url}
unzip ${zip_file}
