# Environment 帮助文档

## 一、 服务器命令
```
gpustat -pui
nvidia-smi

tmux new -s sq
tmux attach -t sq
tmux kill-session -t sq
tmux list-sessions
kill -9 进程号

python test.py
bash run.sh

export HF_ENDPOINT="https://hf-mirror.com"
export CUDA_VISIBLE_DEVICES=0,1,2,3
unset CUDA_VISIBLE_DEVICES

git clone HTTPS链接/SSH链接
wget -P 保存路径 下载网址

unzip ***.zip -d 保存路径
gunzip ***.gz
```



## 二、 GitHub 命令
```
1. 全局配置，在任意位置执行一次即可
git config --global user.email "1213719939@qq.com"
git config --global user.name "SQ1213719939"

2. 进入项目并初始化，执行一次即可
cd 项目名
git init

3. 关联远程仓库，执行一次即可
git remote add origin git@github.com:SQ1213719939/项目名.git

4. 拉取
git pull origin master

5. 添加文件并提交
git add 文件名
git status
git commit -m ""

6.推送
git push -u origin master（首次推送时使用）
git push（之后推送时使用）

7.回退历史
git log --oneline -5
git reset --hard 要回退到的某状态的id

8. 配置 SSH 密钥
ssh-keygen -t ed25519 -C "1213719939@qq.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub（复制SSH）
ssh -T git@github.com
```



## 三、 conda 命令
```
1. 环境：
conda env list
conda create -n *** python=3.8
conda remove -n *** --all
conda create -n new_env --clone old_env

2. 激活、清理缓存：
conda activate ***
conda deactivate
conda clean --all

3. 依赖：
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip list --format=freeze >requirement.txt
//pip：保证包不损坏
//conda：保证版本号对上

4. 镜像：
-i https://pypi.tuna.tsinghua.edu.cn/simple
```



## 四、 已建环境配置

### 4.1  服务器L20

- py310
  - //python=3.10.19, pytorch=2.7.1+cu118
  - 安装PyTorch：
  - pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu118
  - 安装pyg包（https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html，进入run内链接手动下载）：
  - pip install /home/sunqi/torch_scatter-2.1.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_sparse-0.6.18+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_spline_conv-1.2.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install torch_geometric

### 4.2  服务器3090

- py310
  - //python=3.10.18, pytorch=2.7.1+cu118
  - 安装pyg包：
  - pip install /home/sunqi/torch_scatter-2.1.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_sparse-0.6.18+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install /home/sunqi/torch_spline_conv-1.2.2+pt27cu118-cp310-cp310-linux_x86_64.whl
  - pip install torch_geometric

### 4.3  工位电脑

- py310
  - //python=3.10.18, pytorch=2.8.0+cu128
  - pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128

- py38
  - //python=3.8.20, pytorch=2.4.1+cu124
  - pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124



## 五、 服务器账号
1. 55服务器IP：210.30.97.55
2. 215服务器 IP：210.30.97.215
3. L20服务器IP：210.30.97.92
4. Port：51666
5. VPN：v.dlut.edu.cn



## 六、 服务器配置 Anaconda 与 PyTorch
1. 下载 Anaconda 安装脚本​：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
2. 赋予脚本可执行权限：chmod +x Anaconda3-2024.10-1-Linux-x86_64.sh
3. 运行安装脚本：./Anaconda3-2024.10-1-Linux-x86_64.sh
4. 激活 Conda：source ~/.bashrc
5. 重启 IDE，并验证：conda --version
6. 若 conda 命令报错 command not found，运行此命令修复：/home/sunqi/anaconda3/bin/conda init bash
7. 再次激活 Conda：source ~/.bashrc
8. 下载 PyTorch：浏览器搜pytorch.org，找版本号比CUDA Version小的



## 七、GPU与pytorch
- nvidia-smi
- 天选：
  - NVIDIA GeForce RTX 3050 Ti (4G显存)nvi
  - NVIDIA-SMI 566.07 / Driver Version: 566.07 / CUDA Version: 12.7  
- 工位：
  - NVIDIA GeForce RTX 3060 (12G显存)
  - NVIDIA-SMI 572.96 / Driver Version: 572.96 / CUDA Version: 12.8
- 3090显卡
  - NVIDIA GeForce RTX 3090 (24G显存*4)
  - NVIDIA-SMI 535.86.05 / Driver Version: 535.86.05 / CUDA Version: 12.2
- L20显卡
  - NVIDIA L20 (45G显存*8)
  - NVIDIA-SMI 550.163.01 / Driver Version: 550.163.01 / CUDA Version: 12.4
