# Essay 帮助文档

## 1. TAPE（节点分类）

- 配置环境：`pip install transformers==4.16.2`

- 下载数据集：`gpt_respnsers` 中的文件夹名改为小写。

- 缺失数据集：`B. LLM responses` 中 `arxiv_2023` 无法下载，`run.sh` 中删掉 `arxiv_2023`。

- Hugging Face连接超时：`export HF_ENDPOINT="https://hf-mirror.com"`。

- 改源码：`core/LMs/__pycache__/lm_trainer.py` 中第94行 `evaluation_strategy` 改成 `eval_strategy`。

- 改源码：`core/config.py` 中第65行 `cfg.lm.train.batch_size = 9` 改成 `4`。

