class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [1001] * len(nums) 

        jumps[-1] = 0 

        for i in range(len(nums)-2, -1, -1): 
            if nums[i] == 0: 
                continue 
            jumps[i] = min(jumps[i+1:i+nums[i]+1]) + 1
        
        return jumps[0]
