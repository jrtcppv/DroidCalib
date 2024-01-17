.PHONY: build
build:
        docker build -t droidcalib .

.PHONY: run
run:
        docker run --rm -v /home/${USER}/droidimgs:/data -v /home/${USER}/reconstruction:/output --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 droidcalib python demo.py --imagedir=/data --opt_intr --camera_model=mei --reconstruction_path=/output --num_images=300

.PHONY: bash
bash:
        docker run -it --rm -v /home/${USER}/droidimgs:/data -v /home/${USER}/reconstruction:/output --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 droidcalib bash
