# 练习 07: JSON API 客户端

## 目标

从 API 响应中提取学习记录，转换异常信息，并生成汇总。

## 步骤

1. 打开 `api_client.py`。
2. 完成 `fetch_json()`、`extract_records()` 和 `summarize_records()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/07-api-client -v
```

4. 测试会启动本地服务器，不要求外网。

## API 数据格式

```json
{
  "records": [
    {"label": "python", "minutes": 60},
    {"label": "ai", "minutes": 30}
  ]
}
```

## 完成标准

- 三个函数的测试不再跳过。
- 超时和网络错误会转换成 `RuntimeError`。
- HTTP 错误信息包含状态码。
- 非 JSON 响应会触发 `ValueError`。
- 无效记录会被拒绝，合法记录中的文字会去除两侧空格。
