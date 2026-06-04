"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool: 

        # time: O(nlogn)
        # space: 1
        intervals.sort(key=lambda x: x.start)  

        for idx, interval in enumerate(intervals):
            if idx > 0 and intervals[idx-1].end > interval.start: 
                return False 
        return True 




