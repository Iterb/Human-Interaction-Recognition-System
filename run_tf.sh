#!/bin/bash
sudo xhost +
sudo mount /dev/sda4
docker run --rm -it\
	--gpus all \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix/:/tmp/.X11-unix \
	--ipc=host \
	--device=/dev/video0:/dev/video0 \
	-v $(pwd):/workspace \
	-v /media/sebastian/STORAGE_HDD9/data/:/media/sebastian/STORAGE_HDD/data/ \
	-w /workspace \
	har:latest /bin/bash
