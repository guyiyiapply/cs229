# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:10:23 2018

@author: guyia
"""

import pandas as pd
# load the data, in case of the '/'
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/guyia/Desktop/python class/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/Users/guyia/Desktop/python class/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print(ratings.head())

#get the customized table with pivot_table function
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
#print(userRatings.head())

#use the pandas built in function, 'corr()' will compute a correlation score for every column pair in the matrix
corrMatrix = userRatings.corr()
#print(corrMatrix.head())

#drop the movie with less than 100 rated
corrMatrix1 = userRatings.corr(method='pearson', min_periods=100)
print(corrMatrix1.head())

#choose the used ID 0 and drop the missing data
myRatings = userRatings.loc[0].dropna()
print(myRatings)

#recommand the movie to used ID 0, based on the rated information before
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):#for each movie use 0 rated, do the action below
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()# choose the similarity information from the corrMatrix of the target movie
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])#scale the movie with the rated score, x indicate the rated score
                                               # low rated score * similarity = a low recommandation 
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(100))

#some movie is not only similar to one of the movie, this step helps to group the movie which appear more than once
simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

#filter the movie I already seen/rated, this recommandation is meaningless
filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))