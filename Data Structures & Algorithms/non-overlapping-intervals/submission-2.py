class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: 
        # Greedy 
        # time: nlogn 
        # space: n 
        
        intervals = sorted(intervals, key=lambda x: x[0])

        res = 0 
        prev_start, prev_end = intervals[0] 
        for i in range(1, len(intervals)): 
            start, end = intervals[i] 

            if start < prev_end: 
                prev_end = min(prev_end, end) 
                res += 1 
            else: 
                prev_end = end 
        return res 
    