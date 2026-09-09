class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(i: int, arr: List[int] = []) -> None: 
            if i >= len(nums): 
                res.append(arr.copy()) 
                return 
            arr.append(nums[i]) 
            dfs(i+1, arr) 
            arr.pop() 
            dfs(i+1, arr) 
            
        
        dfs(0) 
        return res 
