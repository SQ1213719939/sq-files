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

import numpy
import scipy
import sklearn
print('NumPy版本:', numpy.__version__)
print('SciPy版本:', scipy.__version__)
print('scikit-learn版本:', sklearn.__version__)
