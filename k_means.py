# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:18:42 2018

@author: guyia
"""

from numpy import random, array

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):#generate data
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)#the center point should be in(20000.0, 200000)
        ageCentroid = random.uniform(20.0, 70.0)#the center should be in (20,70)
        for j in range(int(pointsPerCluster)):#in the kth cluster, the jth point is in normal distribution
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

data = createClusteredData(100, 5)

model = KMeans(n_clusters=5)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))


# We can look at the clusters each data point was assigned to
print(model.labels_)

# And we'll visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data[:,0], data[:,1], c=model.labels_)
plt.show()