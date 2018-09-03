# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:00:57 2018

@author: guyia
"""
# load the data
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/guyia/Desktop/python class/u.data', sep='\t', names=r_cols, usecols=range(3))
print(ratings.head())

#calculate the size and the mean of each moive, size: how many people rated, mean: avg rating score
import numpy as np

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print(movieProperties.head())


#the size dose not mean anything, normalize it in (0,1)
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print(movieNormalizedNumRatings.head())

#arrage the data
movieDict = {}
with open(r'C:/Users/guyia/Desktop/python class/u.item') as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))


#distance = genre dis(cosine) + populiraty dis
from scipy import spatial

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance
    
print(ComputeDistance(movieDict[2], movieDict[4]))

print(movieDict[2])
print(movieDict[4])

#for movieDict[4]:
#('Get Shorty (1995)', array([0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
# 0.3567753001715266, 3.550239234449761)
#array indicates the relation between each other,1 indicates they have relation, 0 indivates no relation

import operator

#KNN_coding, first calculate the distance
def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):# the movie is not the target movie
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])#calculate dis
            distances.append((movie, dist))
            print(distances)
    distances.sort(key=operator.itemgetter(1))#use the dis to sort the movies
    
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])# after sorted, get the movie ID
    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)# use getNeihbnors function to get the neighbors
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))
    #movieDict[neighbor][0] indicate the name of the movie
    #movieDict[neighbor][3] indicate the mean rating
avgRating /= K

print(avgRating)
