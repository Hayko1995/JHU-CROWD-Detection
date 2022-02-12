Main sourse code link [Link](https://github.com/dk-liang/FIDTM)

# Environment

if you use pip, for install pytorch use


pip3 install torch==1.10.0+cu102 torchvision==0.11.1+cu102 torchaudio===0.10.0+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html 


command

    python >=3.6
    pytorch >=1.4
    opencv-python >=4.0
    scipy >=1.4.0
    h5py >=2.10
    pillow >=7.0.0
    imageio >=1.18
    nni >=2.0 (python3 -m pip install --upgrade nni)

# Datasets

- Download JHU-CROWD ++ dataset from [here](http://www.crowd-counting.com/)

# Model

Download the pretrained model from [Baidu-Disk](https://pan.baidu.com/s/1SaPppYrkqdWeHueNlcvUJw), passward:gqqm, or [OneDrive](https://1drv.ms/u/s!Ak_WZsh5Fl0lhCneubkIv1mTllAZ?e=0zMHSM)

# Quickly test

Generate FIDT Ground-Truth

```
cd data
run  python fidt_generate_jhu.py
```

Download Dataset and Model  
Generate FIDT map ground-truth

```
Generate image file list: python make_npydata.py
```

**Test example:**

```
python test.py --dataset JHU --pre ./model/JHU/model_best.pth --gpu_id 1
```

**If you want to generate bounding boxes,**

```
python test.py --pre model_best.pth  --visual True
```

**If you want to test a video,**

```
python video_demo.py --pre model_best.pth  --video_path demo.mp4
(the output video will in ./demo.avi; By default, the video size is reduced by two times for inference. You can change the input size in the video_demo.py)
```

More config information is provided in config.py

# Evaluation localization performance

| JHU_Crowd++ <br />(test set) | Precision | Recall | F1-measure |
| :--------------------------: | :-------: | :----: | :--------: |
|             σ=4              |   38.9%   | 38.7%  |   38.8%    |
|             σ=8              |   62.5%   | 62.4%  |   62.4%    |

**Evaluation example:**

```
cd ./local_eval
python eval.py JHU
```

# Training

The training strategy is very simple. You can replace the density map with the FIDT map in any regressors for training.

If you want to train based on the HRNET, please first download the ImageNet pre-trained models from the official [link](https://onedrive.live.com/?authkey=!AKvqI6pBZlifgJk&cid=F7FD0B7F26543CEB&id=F7FD0B7F26543CEB!116&parId=F7FD0B7F26543CEB!105&action=locate), and replace the pre-trained model path in HRNET/congfig.py (\_\_C.PRE_HR_WEIGHTS).

Here, we provide the training baseline code, and the I-SSIM loss will be released when the review is completed.

**Training baseline example:**

```
python train_baseline.py --dataset JHU --crop_size 512 --save_path ./save_file/JHU
```

For ShanghaiTech, you can train by a GPU with 8G memory. For other datasets, please utilize a single GPU with 24G memory or multiple GPU for training. We have reorganized the code, which is usually better than the results of the original [manuscript](https://arxiv.org/abs/2102.07925).

**Improvements**
We have not studied the effect of some hyper-parameter. Thus, the results can be further improved by using some tricks, such as adjust the learning rate, batch size, crop size, and data augmentation.

# Reference

If you find this project is useful for your research, please cite:

```
@article{liang2021focal,
  title={Focal Inverse Distance Transform Maps for Crowd Localization and Counting in Dense Crowd},
  author={Liang, Dingkang and Xu, Wei and Zhu, Yingying and Zhou, Yu},
  journal={arXiv preprint arXiv:2102.07925},
  year={2021}
}
```

# Run Docker

## Please download all files and run second commands

```
docker build -t test
docker run -p 8888:8888 --gpus all -it test
```
