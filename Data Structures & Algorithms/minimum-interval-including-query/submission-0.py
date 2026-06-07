class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Brute force 
        # time: n^2 
        # space: n 

        mp = {}
        for q in queries: 
            for i in intervals: 
                if i[0] <= q <= i[1]: 
                    if q not in mp: 
                        mp[q] = i[1] - i[0] + 1
                    mp[q] = min(mp[q], i[1] - i[0] + 1) 
        
        res = [] 
        for q in queries: 
            if q not in mp: 
                res.append(-1) 
            else: 
                res.append(mp[q]) 
        return res 