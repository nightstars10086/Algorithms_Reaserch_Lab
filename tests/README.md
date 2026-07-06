# tests

这里存放确定型算法的自动化测试。

路径建议：

```text
tests/<topic>/test_<algorithm_name>.py
```

运行全部测试：

```bash
python -m pytest
```

对于 K-means、PCA、遗传算法这类概念实验型算法，不必强行把所有理解都写成单元测试。可以只测试少量稳定性质，例如输出形状、距离函数、损失不增等；主要验证放到 `projects/` 的小型项目中。
