class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        # DP: bottom up 
        # time: n 
        # space: n

        dp = [-1] * len(cost) 

        dp[0], dp[1] = cost[0], cost[1] 

        for i in range(2, len(cost)): 
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])


        
        
        # # DP: memoization 
        # # time: n 
        # # space: n 

        # memo = [-1] * len(cost) 

        # def helper(step: int) -> int: 
        #     if step >= len(cost): 
        #         return 0 
            
        #     if memo[step] != -1: 
        #         return memo[step]

        #     memo[step] = cost[step] + min(helper(step + 1), helper(step + 2)) 
        #     return memo[step]

        # return min(helper(0), helper(1))


        # Brute force 
        # time: 2^n 
        # space: n 

        def helper(step: int) -> int: 
            if step >= len(cost): 
                return 0 
            
            return cost[step] + min(helper(step + 1), helper(step + 2)) 

        return min(helper(0), helper(1))