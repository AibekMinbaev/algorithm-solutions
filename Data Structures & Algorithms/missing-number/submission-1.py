class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0 
        for i in range(len(nums)+1): 
            xor = xor ^ i 
        
        for num in nums: 
            xor = xor ^ num
        
        return xor 



        
        # math: 
        # n = len(nums) 
        # sm = (n * (n + 1)) // 2 

        # for num in nums: 
        #     sm -= num 
        # return sm  