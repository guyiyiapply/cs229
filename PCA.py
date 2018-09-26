# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:49:39 2018

@author: guyia
"""
#use the iris dataset from sklearn
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)# the number of flowers we have
print(numFeatures)# the dimension we have, the length and width of petals and sepals is 4 dims in this data set
print(list(iris.target_names))# the samples can be classifiy into kinds of iris name

X = iris.data
pca = PCA(n_components=3, whiten=True).fit(X)# 4 dims reduct to 2 dim
X_pca = pca.transform(X)

print(pca.components_)# the priciple components stands for eigenvector we use to define the hyperplane
#What we have done is distill our 4D data set down to 2D, by projecting it down to two orthogonal 4D 
#vectors that make up the basis of our new 2D projection. We can see what those 4D vectors are, 
#although it's not something you can really wrap your head around:

#[[ 0.36158968 -0.08226889  0.85657211  0.35884393]
 #[ 0.65653988  0.72971237 -0.1757674  -0.07470647]]
 #the results here shoule be like this, which is not too much meaning to you. you cannot picture four dims
 

print(pca.explained_variance_ratio_)#92%__tell you how much the variance in the original(four dims) is presered 
                                    # as we reduce it into two dims
print(sum(pca.explained_variance_ratio_))#%5
#Although we have thrown away two of our four dimensions, 
#PCA has chosen the remaining two dimensions well enough that we've captured 92% of the variance 
#in our data in a single dimension alone! The second dimension just gives us an additional 5%;
# altogether we've only really lost less than 3% of the variance in our data by projecting it
# down to two dimensions.




#%matplotlib inline
from pylab import *

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):#zip mean chose one by one, i = target_id]
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
pl.legend()
pl.show()
    