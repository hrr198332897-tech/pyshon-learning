# 第 6 课: HTTP API 与 JSON

预计时间: 150 到 210 分钟

## 本课目标

- 使用 `urllib.request` 发起 HTTP GET 请求。
- 设置超时和 `User-Agent`。
- 把 JSON 响应转换为 Python 数据。
- 区分网络错误、HTTP 错误和格式错误。
- 使用本地测试服务器验证网络代码。

## API 请求

API 通常通过 URL 返回 JSON 数据:

```python
from urllib.request import Request, urlopen

request = Request(
    "https://example.com/api/records",
    headers={"User-Agent": "pyshon-learning/1.0"},
)
with urlopen(request, timeout=5.0) as response:
    content = response.read().decode("utf-8")
```

超时可以避免程序无限等待。`User-Agent` 帮助服务方识别请求来源。

## JSON 解析

```python
import json

payload = json.loads(content)
records = payload["records"]
```

不要直接假设响应结构正确。外部数据可能缺少字段、类型不同，甚至根本不是 JSON。

## 错误分层

- `HTTPError`: 服务器返回了错误状态码。
- `URLError`: 连接失败、DNS 失败或网络中断。
- `TimeoutError`: 请求超过指定时间。
- `JSONDecodeError`: 返回内容不是合法 JSON。
- `ValueError`: JSON 合法，但数据结构不符合业务要求。

把这些错误转换成项目自己的错误信息，比让底层异常直接冒到用户界面更清晰。

## 本地测试服务器

测试网络代码时不要依赖公共 API。可以使用 `http.server` 启动临时服务器:

```python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
```

测试服务器可以稳定返回成功、错误和损坏 JSON，让验证不依赖网络状态。

## 示范

运行:

```powershell
python -m unittest discover lessons/06-http-json -v
```

测试会在本机随机端口启动服务器，结束后自动关闭。

## 练习

进入 `exercises/07-api-client/`，完成 `api_client.py`。

## 自检

1. 为什么测试时使用本地服务器比调用真实 API 更可靠？
2. `HTTPError` 和 `URLError` 分别表示什么问题？
3. JSON 格式正确，为什么数据结构仍然可能无效？
