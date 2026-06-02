class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) <= 2: 
            return max(nums) 
        return max(self.helper(nums[0:-1]), self.helper(nums[1:]) ) 
    

    def helper(self, nums: List[int]) -> int: 
        memo = {}
        def dfs(i: int) -> int: 
            if i in memo: 
                return memo[i] 

            if i >= len(nums): 
                return 0

            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i] 
        
        return dfs(0) 
