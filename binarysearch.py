# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:18:14 2018

@author: guyia
"""

#binary serach
def binarysearch(target, nums):
    floor_index=-1
    ceiling_index = len(nums)
    while floor_index+1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_dist = distance/2
        guess_index = floor_index+int(half_dist)
        guess_value = nums[guess_index]
        if target == guess_value:
            return True
        if target < guess_value:
            ceiling_index = guess_index
        else:
            floor_index = guess_index
    return False

print(binarysearch(23,[1,23,34,56,67,69,89]))


        