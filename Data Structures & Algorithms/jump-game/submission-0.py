class Solution:
    def canJump(self, nums: List[int]) -> bool:

        last = len(nums) - 1
        for i in range(len(nums)-1, -1, -1): 
            if last - i <= nums[i]: 
                last = i 
        
        return last == 0
