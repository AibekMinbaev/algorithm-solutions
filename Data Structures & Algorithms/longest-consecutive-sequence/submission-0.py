class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums) 

        res = 0 
        for num in nums: 
            if num - 1 not in nums: 
                cur = 1 
                while num + 1 in nums: 
                    num += 1 
                    cur += 1 
                res = max(res, cur) 
        return res 

