# projects

这里存放小型项目验证，尤其适合 K-means、PCA、梯度下降、遗传算法、神经网络模块等概念实验型算法。

推荐结构：

```text
projects/<topic>/<algorithm_name>/
├── README.md
├── run.py
├── data/
├── outputs/
└── report.md
```

小型项目不是为了做大工程，而是为了回答一个学习问题：我是否真的理解这个算法在真实或半真实场景中的行为？

验证方式可以包括：

- 指标变化
- 可视化结果
- 不同参数对比
- 不同随机种子对比
- 失败案例分析
