import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

clf = GaussianNB()
clf.fit(X, Y)

print("==Predict result by predict==", clf.predict([[-0.8, -1]]))
print("==Predict result by predict_proba==", clf.predict_proba([[-0.8, -1]]))
print("==Predict result by predict_log_proba==", clf.predict_log_proba([[-0.8, -1]]))