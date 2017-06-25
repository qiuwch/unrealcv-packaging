FROM qiuwch/nvidia
ARG unrealcv_version
# Expose version info from the host
# COPY RealisticRendering-Linux-${unrealcv_version}/LinuxNoEditor /home/unrealcv/LinuxNoEditor
COPY LinuxNoEditor /home/unrealcv/LinuxNoEditor
RUN sudo chown -R unrealcv LinuxNoEditor
CMD ./LinuxNoEditor/RealisticRendering/Binaries/Linux/RealisticRendering
