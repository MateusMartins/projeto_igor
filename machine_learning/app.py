import numpy as np
import matplotlib as plot
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn import svm

iris = datasets.load_iris()
clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=10)

print(scores)

