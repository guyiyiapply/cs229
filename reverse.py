# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:49:01 2018

@author: guyia
"""

#use in place to reverse a list
#in_place means no copy of the original list
#decide len() is odd or even
def reverse(nums):
    if len(nums)%2 == 0:
        for i in range(int(len(nums)/2)):
            nums[i],nums[-1-i] = nums[-1-i],nums[i]

    else:
        for j in range(int((len(nums)-1)/2)):
            nums[j],nums[-1-j] = nums[-1-j],nums[j]
    
    return nums


#do not need to decide the odd and even
def reverses(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1
    return list_of_chars
    
print(reverses([1,2,3,4,5,7,8]))


             
            
            
            