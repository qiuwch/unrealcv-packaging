build_name=${1%/}
echo Remove the trailing slash
echo Package contents into a zip file
python ../common/zip.py ${build_name}.zip ${build_name}/LinuxNoEditor
echo Upload binary
# python ../common/gdrive_upload.py ${build_name}.zip
scp ${build_name}.zip qiuwch@gradx.cs.jhu.edu:/users/qiuwch/public_html/release/unrealcv/
