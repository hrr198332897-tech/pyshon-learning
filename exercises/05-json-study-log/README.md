# 练习 05: JSON 学习记录

## 目标

实现一个可以把每日学习时间保存到本地 JSON 文件的小工具。

## 步骤

1. 打开 `study_log.py`。
2. 完成 `save_entries()`、`load_entries()`、`add_entry()` 和 `total_minutes()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/05-json-study-log -v
```

4. 连续运行两次脚本，观察累计分钟数如何变化。

```powershell
python exercises/05-json-study-log/study_log.py
```

本地数据会写入 `data/local/study-log.json`，该目录不会提交到 Git。

## 完成标准

- 四个函数的测试不再跳过。
- 文件不存在时返回空列表。
- 无效 JSON 或错误数据结构会触发 `ValueError`。
- `add_entry()` 不修改传入的原列表。
- 保存后的 JSON 使用 UTF-8 并以换行结尾。
