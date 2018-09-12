# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:04:09 2018

@author: guyia
"""

#permutation palindrome
#permutation: tom,tmo,mot,mto,otm,omt
#palindrome: anna, civic, means at most only one element appear in odd times. others must appear in even times.
#
import collections

def palindrome(num):
    count_nums = collections.Counter(num)# count each elements appear how many times
    values_each_element = list(count_nums.values())# get the values only , we do not care the elements
    
    for i in range(len(values_each_element)):
        values_each_element[i] = values_each_element[i] % 2# get the reminder for each value, odd = 1, even = 0
                                                          
        f = collections.Counter(values_each_element)# count the numbers of 1 and 0 appear
        g = f[1]# get the value of 1 appear
        if g <= 1: # if and only if 1 appear <= one time, it is palindrome
            return True
        else: # others, not
            return False

print(palindrome('abcdcba'))
  
        
        
    
    