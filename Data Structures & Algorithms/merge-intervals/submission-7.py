class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC: nlogn
        # SC: n

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = []
        start, end = intervals[0] 
        for cur_start, cur_end in intervals: 

            if cur_start <= end: 
                end = max(end, cur_end)
            else: 
                res.append([start, end])
                start = cur_start
                end = cur_end 
        res.append([start, end])
        return res  
            


