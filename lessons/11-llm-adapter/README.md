# 第 11 课: 模型服务适配层

预计时间: 180 到 240 分钟

## 本课目标

- 从环境变量读取服务配置。
- 不在代码中硬编码 API key。
- 使用 POST 发送 JSON 请求。
- 把 HTTP、网络、JSON 和业务错误分层处理。
- 把模型调用封装成项目可复用的生成器函数。

## 配置

使用环境变量:

```text
LLM_ENDPOINT=https://example.com/generate
LLM_API_KEY=secret
LLM_MODEL=example-model
```

读取并验证配置:

```python
config = load_config(os.environ)
```

不要把真实密钥写进代码、测试文件或 Git 提交。

## 请求协议

本课使用一个最小通用协议:

```json
{
  "model": "example-model",
  "prompt": "只根据上下文回答问题。"
}
```

成功响应:

```json
{
  "text": "模型生成的回答"
}
```

不同服务商的字段可能不同。适配层的作用就是把外部协议转换为项目内部稳定接口。

## 错误分层

- `HTTPError`: 服务返回错误状态码。
- `URLError`: 网络连接失败。
- `TimeoutError`: 请求超时。
- `JSONDecodeError`: 响应不是 JSON。
- `ValueError`: JSON 合法但缺少 `text` 字段。

## 生成器接口

本地知识搜索只需要一个“提示进入，回答出来”的函数:

```python
generator = make_generator(config)
answer = generator(prompt)
```

这样可以先在本地测试检索，再独立接入模型服务。

## 示范

运行:

```powershell
python -m unittest discover lessons/11-llm-adapter -v
```

测试使用本机临时服务器，不调用真实模型，也不会发送真实密钥。

## 练习

进入 `exercises/12-llm-adapter/`，完成 `llm_adapter.py`。

## 自检

1. 为什么 API key 不能直接写在代码里？
2. 适配层为什么要把服务商 JSON 转成项目自己的格式？
3. 为什么测试应该使用模拟服务，而不是真实模型 API？
