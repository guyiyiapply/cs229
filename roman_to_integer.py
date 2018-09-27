# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:37:27 2018

@author: guyia
"""

#roman to integer

# I:1, V:5, X:10, L:50, C:100, D:500, M:1000

# if left < right, add right and minis 2*left
# same number cannot appear three times continuely
# calculate from left to right

class Solution():
    def roman_to_integer(self,Roman):
        roman_map = {'I':1,' V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        decimal = 0
        
        #decide from left to right
        for i in range(len(Roman)):
            if i > 0 and roman_map[Roman[i]] > roman_map[Roman[i-1]]:
                decimal += roman_map[Roman[i]] - 2* roman_map[Roman[i-1]]
                
            else:
                
                decimal += roman_map[Roman[i]]
            
        return decimal
    
print(Solution().roman_to_integer('MMMCMXCIX'))
            
        