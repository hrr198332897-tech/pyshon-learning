# 第 3 课: 列表、字典与函数

预计时间: 90 到 120 分钟

## 本课目标

- 使用列表保存一组有顺序的数据。
- 使用字典保存键和值的对应关系。
- 使用 `get()` 处理可能不存在的键。
- 使用函数接收并返回列表、字典。
- 使用 `sorted()` 写出确定性的排序结果。

## 列表

列表适合保存有顺序、可以重复的数据:

```python
words = ["python", "ai", "python"]
words.append("github")
print(words[0])
```

## 字典

字典把一个键对应到一个值。统计词频时，单词是键，次数是值:

```python
counts = {}
for word in ["python", "ai", "python"]:
    counts[word] = counts.get(word, 0) + 1
```

`counts.get(word, 0)` 表示: 如果键存在就取值，不存在就返回 `0`。

## 排序

字典本身不适合直接表示“出现最多的词”。先转换成键值对，再排序:

```python
ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
```

`item[1]` 是次数。前面的负号表示从多到少。次数相同时，按单词从 A 到 Z 排序，保证结果稳定。

## 示范

阅读 `example.py`，然后运行:

```powershell
python -m unittest discover lessons/03-lists-dicts-functions -v
```

## 练习

进入 `exercises/04-word-stats/`，完成 `word_stats.py`。

## 自检

1. 为什么字典的 `.get()` 比直接使用 `counts[word]` 更适合统计？
2. 排序键 `lambda item: (-item[1], item[0])` 的两个部分分别控制什么？
3. 函数返回字典和直接打印字典，有什么工程上的区别？
