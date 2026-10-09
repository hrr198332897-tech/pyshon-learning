# 练习 04: 文本词频统计

## 目标

使用列表、字典和函数统计一段英文文本中的词频。

## 步骤

1. 打开 `word_stats.py`。
2. 完成 `count_words()`、`top_words()` 和 `build_summary()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/04-word-stats -v
```

4. 运行脚本:

```powershell
python exercises/04-word-stats/word_stats.py
```

## 规则

- 所有单词转为小写。
- 使用空格分词。
- 去除常见标点符号。
- 词频相同时按字母顺序排序。

## 完成标准

- 三个函数的测试不再跳过。
- 空文本返回 `文本中没有可统计的词。`
- 能解释排序结果为什么是稳定且可重复的。
