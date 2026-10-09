# 练习 09: scikit-learn 分类器

## 目标

完成一次可复现的训练和评估流程。

## 步骤

1. 确保已安装 `requirements.txt`。
2. 打开 `classifier.py`。
3. 完成 `make_dataset()`、`split_dataset()`、`build_model()` 和 `train_and_evaluate()`。
4. 运行测试:

```powershell
python -m unittest discover exercises/09-ml-classifier -v
```

## 完成标准

- 四个函数的测试不再跳过。
- 数据集固定为 120 条、4 个特征。
- 测试集占 25%，并保持类别比例。
- 模型 Pipeline 包含标准化和 `LogisticRegression`。
- 测试准确率至少为 `0.85`。
