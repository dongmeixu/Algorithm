from sklearn.cluster import Birch
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics import calinski_harabaz_score

X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.4, 0.3, 0.4, 0.3], random_state=9)
plt.scatter(X[:, 0], X[:, 1], marker="o")
plt.show()

"""可见如果我们不输入类别数的话，在某些时候BIRCH算法的聚类效果并不一定好，因此这个可选的类别数K一般还是需要调参的。"""
# 不输入可选的类别数K
y_pred = Birch(n_clusters=None).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)

# 由于我们知道数据是4个簇随机产生的，因此我们可以通过输入可选的类别数4来看看BIRCH聚类的输出。
y_pred = Birch(n_clusters=4).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)

"""调节阈值,并不是越小聚类效果越好"""
y_pred = Birch(n_clusters=4, threshold=0.3).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)

y_pred = Birch(n_clusters=4, threshold=0.1).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)

"""和threshold类似，branching_factor不是越小聚类效果越好，需要调参。"""
# 我们基于threshold为0.3的情况，
# 调试下branching_factor，将branching_factor从50降低为20.让BIRCH算法第一阶段的CF Tree规模变大。
y_pred = Birch(n_clusters=4, threshold=0.3, branching_factor=20).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)

y_pred = Birch(n_clusters=4, threshold=0.3, branching_factor=10).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
score = calinski_harabaz_score(X, y_pred)
print(score)
from sklearn.svm import OneClassSVM
OneClassSVM.