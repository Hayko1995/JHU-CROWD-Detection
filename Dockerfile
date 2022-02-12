FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime

COPY . /workspace

RUN pip3 install jupyter notebook
RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN	pip3 install torch==1.10.0+cu102 torchvision==0.11.1+cu102 torchaudio===0.10.0+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]