# 贡献与学习流程

这个仓库主要是个人学习档案，也按小型软件项目的方式维护。

## 开始新任务

1. 用学习任务 Issue 模板建立本周任务。
2. 从 `main` 创建分支，例如 `week/12-api-adapter`。
3. 修改代码和文档。
4. 运行 `python tools/run_checks.py`。
5. 提交 Pull Request 并填写模板。
6. 合并后更新当周学习记录。

## 质量要求

- 新功能应有可运行示例。
- 新逻辑应有测试或明确验证步骤。
- 错误信息应说明问题，而不是只抛出底层异常。
- 不提交密钥、令牌、个人数据或依赖目录。
- 文档与代码行为保持一致。

## Commit 格式

使用“范围: 结果”:

```text
week 12: add model adapter CLI
project: improve knowledge search ranking
docs: add portfolio usage examples
```

## 学习原则

AI 可以帮助解释错误、提出测试和改进建议，但每周至少应保留一次独立完成的实现、运行和复盘。
