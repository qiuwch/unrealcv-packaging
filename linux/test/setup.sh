# All all binaries need to be tested.
url=$1
build_name=$(echo ${url} | sed 's/.*\/\(.*\).zip/\1/')
# name=$(echo ${url} | sed 's/.*\/\(.*\)-Linux.*/\1/')
zip_file=$(echo ${url} | sed 's/.*\/\(.*-Linux.*zip\)/\1/')
echo ${name}
# mkdir ${build_name}
# cd ${build_name}
wget -c ${url}
unzip ${zip_file}
