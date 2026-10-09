# 练习 12: 模型服务适配器

## 目标

实现配置读取、JSON POST 请求、响应校验和生成器封装。

## 步骤

1. 打开 `llm_adapter.py`。
2. 完成 `load_config()`、`build_request()`、`generate()` 和 `make_generator()`。
3. 运行测试:

```powershell
python -m unittest discover exercises/12-llm-adapter -v
```

测试使用本机临时服务，不会访问真实 API。

## 完成标准

- 四个函数的测试不再跳过。
- 缺少任一环境变量时触发 `ValueError`。
- 请求使用 `Bearer` 授权头。
- 请求体包含 `model` 和 `prompt`。
- HTTP 和网络错误转换为 `RuntimeError`。
- 非 JSON 或缺少 `text` 字段时触发 `ValueError`。
