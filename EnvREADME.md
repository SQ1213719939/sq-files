# Environment帮助文档

## 一、环境

（1）工位：198439812

- py310
  - python=3.10.18, pytorch=2.8.0+cu128
  - pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128

- py38
  - python=3.8.20, pytorch=2.4.1+cu124
  - pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

（2）服务器：343813000

- py310
  - python=3.10.18, pytorch=2.7.1+cu118
  - 安装pyg包：
  - pip install /home/sunqi/torch_scatter-2.1.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_sparse-0.6.18+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_spline_conv-1.2.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install torch_geometric```

## 二、服务器
```
IP：210.30.97.55
IP：210.30.97.215
Port：51666
User：sunqi
Pwd：123456
VPN：v.dlut.edu.cn

gpustat -pui

tmux new -s sq
tmux attach -t sq
tmux kill-session -t sq
tmux list-sessions

//export HF_ENDPOINT="https://hf-mirror.com"
//export CUDA_VISIBLE_DEVICES=0,1,2,3
//unset CUDA_VISIBLE_DEVICES
//python test.py
//bash run.sh

git clone https://github.com/***.git
wget -P 保存路径 下载网址
gunzip ***.gz
unzip ***.zip
```

## 三、git命令
```
（1）首次：
cd gnn-notes
git init
git config --global user.email "1213719939@qq.com"
git config --global user.name "SQ1213719939"
git add README.md examples/
git status
git commit -m ""
git remote add origin git@github.com:SQ1213719939/gnn-notes.git
git push -u origin master

（2）后续：
cd gnn-notes
git add README.md examples/
git status
git commit -m ""
git pull origin master  # 新加内容必须先从远程获取内容，与本地内容合并，在没有冲突时，会自动合并。
git push

（3）SSH密钥：
ssh-keygen -t ed25519 -C "1213719939@qq.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com
```

## 四、conda命令
```
（1）conda环境：
conda env list
conda create -n *** python=3.8
conda remove -n *** --all
conda create -n new_env --clone old_env

（2）激活、清理缓存：
conda activate ***
conda deactivate
conda clean --all

（3）依赖：
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip list --format=freeze >requirement.txt
//pip：保证包不损坏
//conda：保证版本号对上

（4）镜像：
-i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 五、GPU与pytorch
```
（1）查看显卡信息：
 //nvidia-smi
· 天选：NVIDIA GeForce RTX 3050 Ti (阵亡)
  天选：NVIDIA-SMI 555.97      Driver Version: 555.97      CUDA Version: 12.5
· 工位：NVIDIA GeForce RTX 3060 (12G显存)
  工位：NVIDIA-SMI 572.96      Driver Version: 572.96      CUDA Version: 12.8
· 服务器：NVIDIA GeForce RTX 3090 (24G显存)
  服务器：NVIDIA-SMI 535.86.05      Driver Version: 535.86.05       CUDA Version: 12.2

（2）下载pytorch：
 //浏览器搜pytorch.org，找版本号比CUDA Version小的

（3）验证：
import torch
import sys
import subprocess
conda_version = subprocess.run(["conda", "--version"], capture_output=True, text=True).stdout.strip()
print("Conda 版本:", conda_version)
print("Python 版本:", sys.version.split()[0])
print("PyTorch 版本:", torch.__version__)
print("CUDA 版本:", torch.version.cuda)
print("CUDA 是否可用:", torch.cuda.is_available())
print("GPU 数量:", torch.cuda.device_count())
print("GPU 名称:", torch.cuda.get_device_name(0))
```
