# AI + Python 学习路线（目录版）

> 说明：正确拼写是 **Python**，不是 "Pyshon"。
> 本文件只是**目录/地图**，用于先看清全程；正式教学会从第一站开始，一课一课来。
> 适用前提：零基础或接近零基础，每周能投入 6~10 小时。按此节奏，走完全程约需 6~9 个月。

---

## 总览：8 个阶段

| 阶段 | 主题 | 周期 | 产出 |
|---|---|---|---|
| 0 | 环境准备与学习姿势 | 1~2 天 | 能跑起第一个 Python 程序 |
| 1 | Python 编程基础 | 3~4 周 | 5 个命令行小工具 |
| 2 | Python 进阶与工程习惯 | 2~3 周 | 1 个带测试的小项目 + GitHub 仓库 |
| 3 | 数据分析三件套 | 3~4 周 | 1 份数据分析图表报告 |
| 4 | 数学基础与机器学习 | 4~6 周 | 1 次 Kaggle 入门赛成绩 |
| 5 | 深度学习入门 | 4~6 周 | 1 个图像/文本模型项目 |
| 6 | 大模型与 AI 应用 | 5~8 周 | 1 个 LLM 应用（问答机器人） |
| 7 | 综合实战与作品集 | 持续 | 3 个作品 + 个人作品集 |

---

## 阶段 0：环境准备与学习姿势（1~2 天）

- 0.1 检查本机 Python 环境（你已装好 Python 3.13，可直接用）
- 0.2 安装并配置 VS Code + Python 插件
- 0.3 认识终端、运行第一个 `hello.py`
- 0.4 什么是虚拟环境（venv）与 pip 安装包
- 0.5 学习方法论：怎么用 AI 提问、怎么记笔记、怎么避免"看懂但写不出"

**验收**：能独立创建虚拟环境、安装一个第三方库、运行一个 .py 文件。

---

## 阶段 1：Python 编程基础（3~4 周）

- 1.1 变量、数据类型、运算符、输入输出
- 1.2 条件判断 `if / elif / else`
- 1.3 循环 `for / while`，`break / continue`
- 1.4 函数：参数、返回值、作用域
- 1.5 容器：列表 list、字典 dict、元组 tuple、集合 set
- 1.6 字符串处理与格式化（f-string）
- 1.7 文件读写（txt / csv / json）
- 1.8 异常处理 `try / except`
- 1.9 模块与包、import 机制
- 1.10 面向对象入门：类、对象、属性、方法、继承

**练习项目（选 5 个）**：猜数字游戏、待办清单、通讯录、简易记账本、文本词频统计、天气查询小程序。

**验收**：不查资料能写出一个 100~200 行的命令行程序，并自己排查报错。

---

## 阶段 2：Python 进阶与工程习惯（2~3 周）

- 2.1 列表/字典推导式
- 2.2 迭代器与生成器
- 2.3 装饰器、闭包（理解即可）
- 2.4 常用标准库：`os`、`pathlib`、`datetime`、`json`、`re`、`collections`
- 2.5 代码规范 PEP 8、类型注解、命名习惯
- 2.6 调试技巧与日志 `logging`
- 2.7 单元测试 `pytest`
- 2.8 Git 与 GitHub：提交、分支、README
- 2.9 项目结构：模块拆分、依赖文件 requirements.txt

**验收**：一个带测试、有 README、能提交到 GitHub 的小项目。

---

## 阶段 3：数据分析三件套（3~4 周）

- 3.1 NumPy：数组、形状、广播、向量化运算
- 3.2 Pandas：Series / DataFrame、索引、筛选
- 3.3 数据清洗：缺失值、重复值、类型转换
- 3.4 分组聚合 `groupby`、表连接 `merge`、透视表
- 3.5 Matplotlib / Seaborn：常用图表与配色
- 3.6 Jupyter Notebook / Google Colab 工作流
- 3.7 探索性数据分析（EDA）的完整套路

**项目**：找一个真实数据集（Kaggle / 国家统计局 / 天气数据），完成清洗 + 分析 + 5 张图表 + 结论报告。

**验收**：能从原始脏数据一路做到"有结论、有图表"的分析报告。

---

## 阶段 4：数学基础与机器学习（4~6 周）

- 4.1 线性代数够用版：向量、矩阵、矩阵乘法
- 4.2 概率统计够用版：均值方差、分布、条件概率、贝叶斯
- 4.3 微积分够用版：导数、偏导、梯度、链式法则
- 4.4 机器学习核心概念：监督/无监督、训练/验证/测试、过拟合与欠拟合
- 4.5 scikit-learn 实战：
  - 线性回归、逻辑回归
  - 决策树、随机森林、梯度提升
  - K-Means 聚类、PCA 降维
- 4.6 评估指标：准确率、精确率、召回率、F1、ROC-AUC、RMSE
- 4.7 特征工程、交叉验证、超参数搜索
- 4.8 完整流程：Pipeline 与数据泄漏防范

**项目**：Kaggle Titanic 生存预测 或 房价预测入门赛。

**验收**：能独立完成一次"数据 → 建模 → 调参 → 评估 → 提交"的闭环。

---

## 阶段 5：深度学习入门（4~6 周）

- 5.1 神经网络原理：感知机、激活函数、损失函数、反向传播
- 5.2 优化器：SGD、Momentum、Adam；学习率
- 5.3 PyTorch 基础：Tensor、autograd、`nn.Module`
- 5.4 训练循环：前向、损失、反向、更新
- 5.5 卷积神经网络 CNN 与图像分类
- 5.6 迁移学习：用预训练模型解决自己的问题
- 5.7 过拟合对策：正则化、Dropout、数据增强、早停
- 5.8 序列模型入门：RNN / LSTM（概念 + 实践）
- 5.9 GPU 与云端算力（Colab / Kaggle Notebook）

**项目**：手写数字识别 / 食物图像分类 / 电影评论情感分析。

**验收**：能读懂一段 PyTorch 训练代码，并改造它训练自己的数据。

---

## 阶段 6：大模型与 AI 应用（5~8 周）

- 6.1 Transformer 与 Attention（概念级理解）
- 6.2 Hugging Face 生态：Transformers、Datasets、Tokenizers
- 6.3 提示工程（Prompt Engineering）与结构化输出
- 6.4 调用大模型 API：OpenAI / 通义 / DeepSeek 等
- 6.5 Embedding 与向量数据库
- 6.6 RAG 检索增强生成：文档切分、检索、拼上下文
- 6.7 微调入门：LoRA / 指令微调（选学）
- 6.8 AI Agent：工具调用、ReAct、多步任务编排
- 6.9 框架：LangChain / LlamaIndex（选一个深入）
- 6.10 应用交付：Streamlit / Gradio 界面，FastAPI + Docker 部署

**项目**：文档问答机器人 / 个人知识库 / 会调用工具的 AI 助手。

**验收**：能做出一个别人可以打开就用的 AI 应用。

---

## 阶段 7：综合实战与作品集（持续）

- 7.1 打磨 3 个作品：数据分析、机器学习、LLM 应用
- 7.2 写高质量 README：问题、方案、结果、截图
- 7.3 Kaggle 比赛与开源贡献
- 7.4 简历与面试中的 AI 项目表达
- 7.5 持续学习：读论文、跟生态更新

---

## 配套资源清单

**Python 基础**
- Python 官方中文文档：https://docs.python.org/zh-cn/3/tutorial/
- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/basic/index.html
- 菜鸟教程 Python：https://www.runoob.com/python/python-tutorial.html

**数学与机器学习**
- Google 机器学习速成课程：https://developers.google.com/machine-learning/crash-course
- DeepLearning.AI 机器学习专项（吴恩达）：https://www.coursera.org/specializations/machine-learning-introduction
- roadmap.sh 机器学习路线图：https://roadmap.sh/machine-learning
- roadmap.sh 数据科学家路线图：https://roadmap.sh/ai-data-scientist

**深度学习**
- 李沐《动手学深度学习》中文版：https://zh.d2l.ai/
- fast.ai 实战深度学习：https://course.fast.ai/
- 哈佛 CS50 人工智能导论（Python）：https://cs50.harvard.edu/ai/

**大模型与应用**
- Hugging Face 大模型课程：https://huggingface.co/learn/llm-course
- Hugging Face Agents 课程：https://huggingface.co/learn/agents-course
- Kaggle Learn 实战小课：https://www.kaggle.com/learn

---

## 我们的上课方式

每一课固定五步：

1. 我讲清概念（尽量用生活例子，不堆术语）
2. 我写代码演示
3. 你亲手改一改、写一写
4. 我批改并指出改进点
5. 留一道小练习，下节课检查

进度可以随时调整：卡住就多停，学得快就加速。
