# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:18:14 2018

@author: guyia
"""
# there are 4 sections here
# fit the model with one training /one testing
#use linear kernel and k cross fold(k = 5)
# use poly kernel and k cross fold (k=5), not good as linear, indicates overfitting
# use poly to do the 1 train and 1 test fitted model 

import numpy as np
#cross_val_score is for k cross fold
#train_test_split is for one train and one test
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm
# use iris data set, take care of the data sturcture
iris = datasets.load_iris()

# Split the iris data into train/test data sets with 40% reserved for testing, iris.data is the X, iris.target is the y
#X is the features of the iris, y is the gerne of the iris
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

# Build an SVC model for predicting iris classifications using training data
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

#plot the data, not too much meaning , X is 90*4 metrix
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(X_train[:,0], X_train[:,1], c=y_train.astype(np.float))
plt.show()

# Now measure its performance with the test data, task 0ne
print(clf.score(X_test, y_test))



# We give cross_val_score a model, the entire data set and its "real" values, and the number of folds:
scores = cross_val_score(clf, iris.data, iris.target, cv=5)

# Print the accuracy for each fold:
print(scores)#task 2

# And the mean accuracy of all 5 folds:
print(scores.mean())#task 2

clf = svm.SVC(kernel='poly', C=1).fit(X_train, y_train)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(scores.mean())#task 3 

# Build an SVC model for predicting iris classifications using training data
clf = svm.SVC(kernel='poly', C=1).fit(X_train, y_train)

# Now measure its performance with the test data
clf.score(X_test, y_test) #task 4