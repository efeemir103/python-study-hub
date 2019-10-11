#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sklearn
from sklearn import datasets
from sklearn import metrics
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

# print(cancer.feature_names)
# print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection. \
    train_test_split(x, y, test_size = 0.2)

# print(x_train, y_train)
classes = ['malignent', 'benign']

# clf = svm.SVC(kernel = 'poly', gamma = 'auto')
clf = KNeighborsClassifier(n_neighbors = 9)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)