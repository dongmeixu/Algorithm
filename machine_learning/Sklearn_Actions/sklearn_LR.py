"""
　在scikit-learn中，与逻辑回归有关的主要是这3个类。LogisticRegression， LogisticRegressionCV 和logistic_regression_path。

  其中LogisticRegression和LogisticRegressionCV的主要区别是LogisticRegressionCV使用了交叉验证来选择正则化系数C。
  而LogisticRegression需要自己每次指定一个正则化系数。
  除了交叉验证，以及选择正则化系数C以外， LogisticRegression和LogisticRegressionCV的使用方法基本相同。

　　　　
  logistic_regression_path类则比较特殊，它拟合数据后，不能直接来做预测，只能为拟合数据选择合适逻辑回归的系数和正则化系数。
  主要是用在模型选择的时候。一般情况用不到这个类，所以后面不再讲述logistic_regression_path类。


　此外，scikit-learn里面有个容易让人误解的类RandomizedLogisticRegression,虽然名字里有逻辑回归的词，
  但是主要是用L1正则化的逻辑回归来做特征选择的，属于维度规约的算法类，不属于我们常说的分类算法的范畴。

"""
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, RandomizedLogisticRegression
"""
3. 优化算法选择参数：solver
    solver参数决定了我们对逻辑回归损失函数的优化方法，有4种算法可以选择，分别是：除a以外剩下的优化算法都需要损失函数连续可导

　　　　a) liblinear：使用了开源的liblinear库实现，内部使用了坐标轴下降法来迭代优化损失函数。

　　　　b) lbfgs：拟牛顿法的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。

　　　　c) newton-cg：也是牛顿法家族的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。

　　　　d) sag：即随机平均梯度下降，是梯度下降法的变种，和普通梯度下降法的区别是每次迭代仅仅用一部分的样本来计算梯度，适合于样本数据多的时候。

        对于多元逻辑回归常见的有one-vs-rest(OvR)和many-vs-many(MvM)两种。而MvM一般比OvR分类相对准确一些。
        郁闷的是liblinear只支持OvR，不支持MvM，这样如果我们需要相对精确的多元逻辑回归时，就不能选择liblinear了。
        也意味着如果我们需要相对精确的多元逻辑回归不能使用L1正则化了。
"""

import pandas as pd

data = pd.read_csv("./data/diabetes.csv")
print(data.head())
print(data.info())
print(data.describe())