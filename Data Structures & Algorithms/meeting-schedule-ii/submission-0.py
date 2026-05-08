"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int: 
        starts = [] 
        ends = [] 

        for interval in intervals: 
            starts.append(interval.start) 
            ends.append(interval.end) 
        
        starts.sort() 
        ends.sort()  
        
        res = 0 
        cnt = 0 
        s, e = 0, 0 
        while s < len(intervals): 
            if starts[s] < ends[e]: 
                cnt += 1 
                s += 1 
            else: 
                cnt -= 1 
                e += 1 
            res = max(res, cnt)  
        return res 

