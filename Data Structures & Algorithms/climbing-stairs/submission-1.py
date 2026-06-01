class Solution:
    def climbStairs(self, n: int) -> int:
        # DP memoization  
        # time: n 
        memo = [-1] * (n + 1)

        def helper(step: int) -> int:
            if step > n: 
                return 0 
            
            if step == n: 
                return 1

            if memo[step] != -1: 
                return memo[step]

            memo[step] = helper(step + 1) + helper(step + 2) 
            return memo[step]
        
        return helper(0)



        # # Brute Force 
        # # time: 2^n

        # def helper(step: int) -> int:
        #     if step > n: 
        #         return 0 
            
        #     if step == n: 
        #         return 1

        #     return helper(step + 1) + helper(step + 2) 
        
        # return helper(0)