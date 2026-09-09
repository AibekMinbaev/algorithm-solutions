class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        sm = (n * (n + 1)) // 2 

        for num in nums: 
            sm -= num 
        return sm  