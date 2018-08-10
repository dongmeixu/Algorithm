import numpy as np
import pandas as pd

data = pd.read_csv("data/diabetes.csv")

X = data.iloc[:, 0: 8]
y = data.iloc[:, 8]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier

model_1 = KNeighborsClassifier(n_neighbors=2, weights="uniform")
model_1.fit(x_train, y_train)
score_1 = model_1.score(x_test, y_test)

model_2 = KNeighborsClassifier(n_neighbors=2, weights="distance")
model_2.fit(x_train, y_train)
score_2 = model_2.score(x_test, y_test)

model_3 = RadiusNeighborsClassifier(n_neighbors=2, radius=500.0)
model_3.fit(x_train, y_train)
score_3 = model_3.score(x_test, y_test)

print(score_1, score_2, score_3)

from sklearn.model_selection import cross_val_score

result1 = cross_val_score(model_1, X, y, cv=10)
result2 = cross_val_score(model_2, X, y, cv=10)
result3 = cross_val_score(model_3, X, y, cv=10)
print(result1.mean(), result2.mean(), result3.mean())

predict1 = model_1.predict(x_test)
print(predict1)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predict1)
print(cm)

###########################################
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_classification

# X为样本特征，Y为样本类别输出， 共1000个样本，每个样本2个特征，输出有3个类别，没有冗余特征，每个类别一个簇
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_clusters_per_class=1, n_classes=3)
plt.scatter(X[:, 0], X[:, 1], marker="o", c=y)
plt.show()

# 用KNN来拟合模型，我们选择K=15，权重为距离远近
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=15, weights="distance")
clf.fit(X, y)

# 可视化预测效果
from matplotlib.colors import ListedColormap

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# 确认训练集的边界
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# 生成随机数据来做测试集，然后作预测
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# 画出测试集数据
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# 也画出所有的训练集数据
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class classification (k = 15, weights = 'distance')")
plt.show()