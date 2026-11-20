# Day 75 · scikit-learn Pipeline

> 阶段：AI｜AI / 机器学习 / LLM

## 学习目标

- 掌握 Pipeline 组装流程
- 掌握列变换 ColumnTransformer
- 掌握模型持久化

## 今日知识点

- Pipeline([("scaler",...),("clf",...)])
- ColumnTransformer 分列处理
- joblib.dump / load
- 与交叉验证结合

## 实践任务

1. 把标准化+分类组成 Pipeline
2. 用 ColumnTransformer 分别处理数值/类别列
3. 训练后保存模型并重新加载预测

## 验收标准

- Pipeline 可正常 fit/predict
- 分列处理生效
- 模型持久化后预测一致

## 推荐资源

- https://scikit-learn.org/stable/modules/compose.html

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：
