# 练习 11: RAG 上下文构造

## 目标

把长文本切分为带重叠的块，并构造只使用指定来源的回答提示。

## 步骤

1. 打开 `rag_context.py`。
2. 完成 `chunk_text()`、`normalize_chunks()` 和 `build_prompt()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/11-rag-context -v
```

## 完成标准

- 三个函数的测试不再跳过。
- `overlap` 不小于 `max_chars` 时触发 `ValueError`。
- 空文本返回空列表。
- 空块会被清理。
- 上下文中保留 `[1]`、`[2]` 来源编号。
- 提示明确要求在上下文不足时回答“不知道”。
