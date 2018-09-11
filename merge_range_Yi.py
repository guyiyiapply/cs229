# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:46:08 2018

@author: guyia
"""
# given [(0,1),(0,5),(4,8),(10,12),(9,10)]
#return [(0, 8), (9, 12)] like schdele a meeting

#Time complexity: O(nlogn), sorted
#space:O(n)

def mergeranges(meetings):
    #sort the meeting with start time
    sorted_meetings = sorted(meetings)
    #save the first one as a start of the merged meeting range
    merged_meetings = [sorted_meetings[0]]
    
    #current_meeting is the one we decide to merge, last is the one already merged
    #as initial, the last is the (0,1), the current is (0,5)
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_meeting_start,last_meeting_end = merged_meetings[-1]
        
        #if they have overlap, save the bigger one of two tests
        if last_meeting_end >= current_meeting_start:
            merged_meetings[-1] = (last_meeting_start,max(current_meeting_end,last_meeting_end))
        #no overlap, just append
        else:
            merged_meetings.append((current_meeting_start,current_meeting_end))
            
    return merged_meetings

print(mergeranges([(0,1),(0,5),(4,8),(10,12),(9,10)]))
            
        
    
    