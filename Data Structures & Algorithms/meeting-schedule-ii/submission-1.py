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
        
        max_rooms = 0 
        rooms = 0 
        s, e = 0, 0 
        while s < len(intervals): 
            if starts[s] < ends[e]: 
                rooms += 1 
                s += 1 
            else: 
                rooms -= 1 
                e += 1 
            max_rooms = max(max_rooms, rooms)  
        return max_rooms 

