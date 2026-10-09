# 第 9 课: TF-IDF 文本检索

预计时间: 150 到 210 分钟

## 本课目标

- 理解文档、查询和检索结果。
- 使用 `TfidfVectorizer` 把文本转换为向量。
- 使用余弦相似度比较查询和文档。
- 对结果排序并保留来源。
- 为后续 RAG 应用准备上下文片段。

## 为什么先做检索

大模型本身不知道你的私人资料。常见解决方式:

1. 把资料保存为文档。
2. 根据问题找到最相关文档。
3. 把相关文档作为上下文交给模型。
4. 要求模型只根据上下文回答。

本课先完成最关键的第二步。

## 向量化

TF-IDF 会降低常见词的影响，提高有区分度词语的权重:

```python
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
matrix = vectorizer.fit_transform(documents)
```

## 相似度

查询也要用同一个向量器转换:

```python
query_vector = vectorizer.transform([query])
scores = cosine_similarity(query_vector, matrix).ravel()
```

分数越接近 `1`，查询与文档越相似。

## 排序

```python
ranked = sorted(
    enumerate(scores),
    key=lambda item: (-item[1], item[0]),
)
```

次数相同时按原始文档顺序排列，保证结果稳定。

## 示范

运行:

```powershell
python -m unittest discover lessons/09-tfidf-retrieval -v
```

## 练习

进入 `exercises/10-document-search/`，完成 `document_search.py`。

## 自检

1. 为什么查询和文档必须使用同一个向量器转换？
2. 余弦相似度高是否代表答案一定正确？
3. 构建给模型的上下文时，为什么需要保留来源编号？
