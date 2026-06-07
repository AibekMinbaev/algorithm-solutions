class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0]) 

        res = [intervals[0]]
        for i in range(1, len(intervals)): 
            prev_start, prev_end = res[-1]
            start, end = intervals[i] 
            if start <= prev_end: 
                res.pop()
                res.append([min(start, prev_start), max(prev_end, end)]) 
            else: 
                res.append([start, end]) 
        return res 
