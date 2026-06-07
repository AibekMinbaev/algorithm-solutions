"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int: 

        # Brute force: 
        # time: n^2 
        # space: n 
        intervals = sorted(intervals, key=lambda x: x.start) 

        ends = []
        for interval in intervals: 
            for i in range(len(ends)): 
                if ends[i] <= interval.start: 
                    ends[i] = interval.end 
                    break 
            else: 
                ends.append(interval.end) 
        return len(ends) 
            


