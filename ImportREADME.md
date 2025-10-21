# Import帮助文档

## 一、常用库
```python
import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt  # 作图
from sklearn.manifold import TSNE  # t-SNE非线性降维
```

## 二、数据库
```python
# Cora, Citeseer, Pubmed, Reddit
from torch_geometric.datasets import Planetoid
from torch_geometric.transforms import NormalizeFeatures
from torch_geometric.datasets import Reddit
cora = Planetoid(root='', name='Cora', transform=NormalizeFeatures())
citeseer = Planetoid(root='', name='Citeseer', transform=NormalizeFeatures())
pubmed = Planetoid(root='', name='Pubmed', transform=NormalizeFeatures())
reddit = Reddit(root='')

# ogbn_arxiv、ogbn_products
from ogb.nodeproppred import PygNodePropPredDataset
from ogb.linkproppred import PygLinkPropPredDataset
from ogb.graphproppred import PygGraphPropPredDataset
ogbn_arxiv = PygNodePropPredDataset(name='ogbn-arxiv', root='')
ogbn_products = PygNodePropPredDataset(name='ogbn-products', root='')
```
