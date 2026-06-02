class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: bottom up 

        if len(nums) <= 2: 
            return max(nums) 
        
        dp = [0] * len(nums) 
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)): 
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]) 
        
        return dp[len(nums)-1]

        
        # DP: memoization
        # time: n 

        # memo = {}
        # def helper(i: int) -> int: 
        #     if i in memo: 
        #         return memo[i] 

        #     if i >= len(nums): 
        #         return 0

        #     memo[i] = max(nums[i] + helper(i+2), helper(i+1))
        #     return memo[i]
        # return helper(0)

        # # Brute force 
        # # time: 2^n 

        # def helper(i: int) -> int: 
        #     if i >= len(nums): 
        #         return 0 
            
        #     return max(nums[i] + helper(i+2), helper(i+1))

        # return helper(0)