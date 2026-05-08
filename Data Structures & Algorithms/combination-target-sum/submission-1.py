class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(i: int, arr: List[int], t: int): 
            if t == 0: 
                res.append(arr.copy()) 
                return 
            
            if i >= len(nums) or t < 0: 
                return 
            
            arr.append(nums[i])
            dfs(i, arr, t - nums[i]) 

            arr.pop() 
            dfs(i+1, arr, t) 
            
        dfs(0, [], target)
        return res 
