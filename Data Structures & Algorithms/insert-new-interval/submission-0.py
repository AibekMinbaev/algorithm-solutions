class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # time: O(n) 
        # space: O(1) 

        res = []
        curr_start, curr_end = newInterval
        for start, end in intervals: 
            if curr_start > end: 
                res.append([start,end]) 
            elif start > curr_end: 
                res.append([curr_start,curr_end]) 
                curr_start, curr_end = start, end 
            else: 
                curr_start = min(curr_start, start) 
                curr_end = max(curr_end, end) 

        res.append([curr_start, curr_end]) 
        return res 


