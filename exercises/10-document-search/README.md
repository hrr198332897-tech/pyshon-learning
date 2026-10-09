# 练习 10: 本地文档搜索

## 目标

使用 TF-IDF 和余弦相似度实现稳定的本地文档检索。

## 步骤

1. 确保已安装 `requirements.txt`。
2. 打开 `document_search.py`。
3. 完成 `build_index()`、`search_documents()` 和 `build_context()`。
4. 运行测试:

```powershell
python -m unittest discover exercises/10-document-search -v
```

## 完成标准

- 三个函数的测试不再跳过。
- 空文档或空查询会触发 `ValueError`。
- 搜索结果包含原始索引、分值和文本。
- 分值相同时按原始顺序排列。
- 上下文使用 `[1]`、`[2]` 编号。
- 没有相关文档时返回 `没有找到相关内容。`
