"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:  
        start = sorted([i.start for i in intervals]) 
        end = sorted([i.end for i in intervals]) 

        res, count = 0, 0 
        s, e = 0, 0 
        while s < len(start): 
            if start[s] < end[e]: 
                count += 1 
                s += 1 
            else: 
                count -= 1 
                e += 1
            res = max(res, count) 
        return res 
        
        # # Min Heap: Simulation
        # # time: nlogn 
        # # space: n 
        # intervals = sorted(intervals, key=lambda x: x.start) 

        # rooms = []
        # res = 0 
        # for interval in intervals: 
        #     if rooms and rooms[0] <= interval.start: 
        #         heapq.heappop(rooms) 
        #     heapq.heappush(rooms, interval.end) 
        #     res = max(res, len(rooms))
        # return res

        # # Brute force: 
        # # time: n^2 
        # # space: n 
        # intervals = sorted(intervals, key=lambda x: x.start) 

        # ends = []
        # for interval in intervals: 
        #     for i in range(len(ends)): 
        #         if ends[i] <= interval.start: 
        #             ends[i] = interval.end 
        #             break 
        #     else: 
        #         ends.append(interval.end) 
        # return len(ends) 
            


