import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics import calinski_harabaz_score
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=100, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)

print(X.shape, y.shape)
plt.scatter(X[:, 0], X[:, 1], marker="o")
plt.show()

"""kmeans"""
y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

score = calinski_harabaz_score(X, y_pred)
print(score)


y_pred = KMeans(n_clusters=3, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

score = calinski_harabaz_score(X, y_pred)
print(score)


y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

score = calinski_harabaz_score(X, y_pred)
print(score)

"""minibatch-kmeans"""
for index, k in enumerate((2, 3, 4, 5)):
    plt.subplot(2, 2, index + 1)
    y_pred = MiniBatchKMeans(n_clusters=k, batch_size=200, random_state=9).fit_predict(X)
    score = calinski_harabaz_score(X, y_pred)
    plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    plt.text(.99, .01, ("k=%d, score:%.2f" % (k, score)),
             transform=plt.gca().transAxes, size=10, horizontalalignment="right")
    print(score)
plt.show()