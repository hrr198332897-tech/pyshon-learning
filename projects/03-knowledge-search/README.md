# 项目 3: 本地知识搜索

这个项目把文档加载、文本分块、TF-IDF 索引、相似度检索和来源引用组合成一个可运行的本地知识搜索工具。

## 功能

- 扫描目录中的 `.md` 和 `.txt` 文件。
- 使用重叠窗口切分长文档。
- 为中文和英文建立字符级 TF-IDF 索引。
- 返回最相关片段、来源文件和片段编号。
- 没有相关内容时明确回答“不知道”。
- 提供可插拔 `generator`，后续可以接入真实大模型。

## 运行

进入项目目录:

```powershell
Set-Location projects/03-knowledge-search
python -m knowledge_search --query "RAG 是什么"
```

显示检索上下文:

```powershell
python -m knowledge_search --query "RAG 是什么" --show-context
```

指定自己的文档目录:

```powershell
python -m knowledge_search --documents C:\path\to\notes --query "你的问题"
```

## 代码结构

| 文件 | 职责 |
| --- | --- |
| `knowledge_search/documents.py` | 文档扫描和重叠分块 |
| `knowledge_search/index.py` | TF-IDF 索引与相似度检索 |
| `knowledge_search/answer.py` | 提示构造、检索式回答和模型边界 |
| `knowledge_search/cli.py` | 命令行入口 |

## 测试

```powershell
Set-Location projects/03-knowledge-search
python -m unittest discover -v
```

## 后续接入大模型

`answer_question()` 接受一个 `generator` 回调。回调只接收已经构造好的、带来源编号的提示。这样可以先独立验证检索质量，再接入 API，避免把网络错误、模型错误和检索错误混在一起。
