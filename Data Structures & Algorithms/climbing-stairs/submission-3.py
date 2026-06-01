class Solution:
    def climbStairs(self, n: int) -> int:
        # DP bottom up
        # time: n 
        # space: n 
        dp = [0] * (n + 1) 

        dp[0], dp[1] = 1, 1 
        for i in range(2, n+1): 
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


        # # DP memoization  
        # # time: n 
        # # space: n 
        # memo = [-1] * (n + 1)

        # def helper(step: int) -> int:
        #     if step > n: 
        #         return 0 
            
        #     if step == n: 
        #         return 1

        #     if memo[step] != -1: 
        #         return memo[step]

        #     memo[step] = helper(step + 1) + helper(step + 2) 
        #     return memo[step]
        
        # return helper(0)


        # # Brute Force 
        # # time: 2^n

        # def helper(step: int) -> int:
        #     if step > n: 
        #         return 0 
            
        #     if step == n: 
        #         return 1

        #     return helper(step + 1) + helper(step + 2) 
        
        # return helper(0)