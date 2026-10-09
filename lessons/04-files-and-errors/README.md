# 第 4 课: 文件、JSON 与异常

预计时间: 120 到 180 分钟

## 本课目标

- 使用 `pathlib.Path` 表示文件路径。
- 使用 `write_text()` 和 `read_text()` 读写文本。
- 使用 `json` 保存列表和字典。
- 使用 `try`、`except`、`raise` 处理错误。
- 使用临时目录测试文件操作，不污染项目目录。

## 路径

`Path` 可以组合路径并检查文件是否存在:

```python
from pathlib import Path

path = Path("data/local/study-log.json")
print(path.exists())
```

创建父目录并写入文件:

```python
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("hello", encoding="utf-8")
```

## JSON

JSON 适合保存结构化数据:

```python
import json

entries = [{"day": 1, "minutes": 60}]
text = json.dumps(entries, ensure_ascii=False, indent=2)
loaded = json.loads(text)
```

`ensure_ascii=False` 让中文保持可读，`indent=2` 让文件更容易查看。

## 异常

处理预期错误:

```python
try:
    minutes = int("abc")
except ValueError as exc:
    raise ValueError("minutes must be an integer") from exc
```

主动拒绝无效数据:

```python
if minutes < 0:
    raise ValueError("minutes cannot be negative")
```

不要把异常全部吞掉。`except` 应处理你真正理解的错误，并把无法恢复的问题继续交给上层。

## 示范

运行:

```powershell
python -m unittest discover lessons/04-files-and-errors -v
```

`example.py` 使用临时目录，因此测试结束后不会留下练习文件。

## 练习

进入 `exercises/05-json-study-log/`，完成 `study_log.py`。

## 自检

1. 为什么读取 JSON 后还要检查它是不是列表？
2. `from exc` 保留了哪一部分信息？
3. 测试文件读写时，为什么临时目录比写入仓库根目录更合适？
