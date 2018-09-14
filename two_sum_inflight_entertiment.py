# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:56:23 2018

@author: guyia
"""

#inflight entertement system the total time of two movies should be equal to the flight time
#as two sum problems

#O(nlogn)
def two_sum(nums, target):
    movies = sorted(nums)
    movie_start_index = 0
    movie_end_index = len(movies)-1
 
    # after sort, the sum = the most left + the most right. less than target, move the left to right.
    while movie_start_index < movie_end_index:
        if movies[movie_start_index] + movies[movie_end_index] < target:
            movie_start_index += 1
            
        elif movies[movie_start_index] + movies[movie_end_index] > target:
            movie_end_index -= 1
            
        else:
            return True
        
    return False

print(two_sum([12,15,24,34,18,45,78,34,23],100))
        
    