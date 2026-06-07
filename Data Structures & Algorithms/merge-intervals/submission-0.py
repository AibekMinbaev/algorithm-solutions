class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0]) 

        res = [intervals[0]]
        for i in range(1, len(intervals)): 
            prev_start, prev_end = res.pop()
            start, end = intervals[i] 

            if start <= prev_end: 
                start = min(start, prev_start) 
                end = max(end, prev_end) 
                res.append([start, end]) 
            else: 
                res.append([prev_start, prev_end]) 
                res.append([start, end]) 
        return res 
