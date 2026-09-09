class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        hp = [] 

        res = [] 
        for i in range(k-1): 
            heapq.heappush(hp, (-nums[i], i)) 
        
        for r in range(k-1, len(nums)): 
            heapq.heappush(hp, (-nums[r], r)) 
            
            while hp and hp[0][1] < r - k + 1 : 
                heapq.heappop(hp) 
            
            mx = -hp[0][0]
            res.append(mx) 

        return res 
