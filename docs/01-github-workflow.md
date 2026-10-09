# GitHub 学习工作流

GitHub 不只是保存代码的地方。这个仓库用它记录每次可验证的进步。

## 一次性设置

在 GitHub 创建名为 `pyshon-learning` 的空仓库后，先配置提交身份:

```powershell
git config --global user.name "你的 GitHub 用户名"
git config --global user.email "你的 GitHub 验证邮箱"
```

连接远程仓库:

```powershell
git remote add origin https://github.com/你的用户名/pyshon-learning.git
git push -u origin main
```

不要提交密钥、令牌、个人隐私数据或从网站保存的完整课程页面。

## 每周流程

```powershell
git switch -c week/01-python-basics
```

学习、练习、运行和修改完成后:

```powershell
git status
git add .
git commit -m "week 01: complete first Python script"
git push -u origin week/01-python-basics
```

在 GitHub 创建 Pull Request，检查改动并写出本周结论，然后合并到 `main`。

## Commit 写法

使用“范围: 结果”的形式，描述完成了什么:

- `week 01: add environment check`
- `week 02: implement number guessing game`
- `week 05: read and summarize CSV data`
- `project: add usage examples`

避免使用 `update`、`changes`、`work` 这类无法说明内容的提交信息。

## 每周应检查

- 代码是否可以从干净环境运行。
- README 是否说明输入、输出和运行命令。
- 是否泄露 API key 或个人信息。
- 是否记录了遇到的错误和解决方法。
- 是否有一个明确的学习成果，而不是只留下笔记。
