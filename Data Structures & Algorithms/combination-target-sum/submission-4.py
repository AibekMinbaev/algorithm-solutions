class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # backtracking 
        # time: 2^t/m, because max height of tree can be t / m smallest value
        # space: 2^t/m
        
        res = [] 
        curr = [] 

        def dfs(i: int, sm: int) -> None: 
            if i >= len(nums): 
                return 

            if sm == target: 
                res.append(curr.copy()) 
                return 
            
            if sm > target: 
                return 
            
            curr.append(nums[i])
            dfs(i, sm + nums[i]) 
            curr.pop() 
            dfs(i+1, sm) 

        dfs(0, 0) 
        return res 