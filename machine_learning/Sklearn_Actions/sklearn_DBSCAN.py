"""

密度聚类

"""
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

x1, y1 = datasets.make_circles(n_samples=5000, factor=.6, noise=.05)
x2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2, 1.2]],
                             cluster_std=[[.1]], random_state=9)

X = np.concatenate([x1, x2])
plt.scatter(X[:, 0], X[:, 1], marker='o')
plt.show()

from sklearn.cluster import KMeans, DBSCAN

# kmeans聚类效果------对非凸数据集的聚类效果不好
y_pred = KMeans(n_clusters=3, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

# 1. DBSCAN
y_pred = DBSCAN().fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()


# 2. 类别数太少，我们需要增加类别数，
#    那么我们可以减少ϵϵ-邻域的大小，默认是0.5，我们减到0.1看看效果。
y_pred = DBSCAN(eps=0.1).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

# 3. 此时我们需要继续调参增加类别，有两个方向都是可以的，一个是继续减少eps，另一个是增加min_samples。
#    我们现在将min_samples从默认的5增加到10
y_pred = DBSCAN(eps=0.1, min_samples=10).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
"""
min_samples： DBSCAN算法参数，即样本点要成为核心对象所需要的ϵϵ-邻域的样本数阈值。
              默认值是5. 一般需要通过在多组值里面选择一个合适的阈值。
              通常和eps一起调参。
              1. 在eps一定的情况下，min_samples过大，则核心对象会过少，此时簇内部分本来是一类的样本可能会被标为噪音点，类别数也会变多。
              ps:核心对象过少，则密度可达的样本点一般会减少，这样紧密相连的一个类别的样本数就会少，自然聚类类别数就变多。
              2. 反之min_samples过小的话，则会产生大量的核心对象，可能会导致类别数过少。
"""