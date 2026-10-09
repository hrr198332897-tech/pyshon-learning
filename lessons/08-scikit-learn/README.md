# 第 8 课: scikit-learn 机器学习入门

预计时间: 180 到 240 分钟

## 本课目标

- 理解特征、标签、训练集和测试集。
- 使用 `make_classification()` 生成可复现数据。
- 使用 `train_test_split()` 划分数据。
- 使用 Pipeline 组合标准化和分类器。
- 使用准确率评估模型。

## 特征与标签

机器学习模型需要两组数据:

- 特征: 用来预测的输入。
- 标签: 希望模型学会预测的答案。

```python
features, labels = make_classification(
    n_samples=120,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    random_state=42,
)
```

## 划分数据

不能使用训练数据进行最终评估，否则结果会偏向模型见过的问题:

```python
train_x, test_x, train_y, test_y = train_test_split(
    features,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)
```

`stratify=labels` 保持训练集和测试集中的类别比例接近。

## Pipeline

Pipeline 把预处理和模型连接成一条流程:

```python
model = Pipeline(
    [
        ("scale", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
```

这样测试数据会使用与训练数据相同的标准化方式。

## 评估

```python
accuracy = model.score(test_x, test_y)
```

准确率适合类别均衡的入门问题。类别极不平衡时，还需要精确率、召回率和 F1。

## 示范

运行:

```powershell
python -m unittest discover lessons/08-scikit-learn -v
```

如果缺少 scikit-learn，测试会跳过；安装 `requirements.txt` 后会自动执行。

## 练习

进入 `exercises/09-ml-classifier/`，完成 `classifier.py`。

## 自检

1. 为什么不能用训练数据作为最终评估数据？
2. `random_state` 对可复现实验有什么作用？
3. Pipeline 中的标准化为什么也要应用到测试数据？
