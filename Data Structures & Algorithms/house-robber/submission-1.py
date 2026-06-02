class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: memoization
        # time: 2^n 

        memo = {}
        def helper(i: int) -> int: 
            if i in memo: 
                return memo[i] 

            if i >= len(nums): 
                return 0
                 
            memo[i] = max(nums[i] + helper(i+2), helper(i+1))
            return memo[i]
        return helper(0)


        # # Brute force 
        # # time: 2^n 

        # def helper(i: int) -> int: 
        #     if i >= len(nums): 
        #         return 0 
            
        #     return max(nums[i] + helper(i+2), helper(i+1))

        # return helper(0)