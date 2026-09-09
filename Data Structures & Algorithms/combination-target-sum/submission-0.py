class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def helper(i: int, arr: List[int], t: int): 
            if t == 0: 
                res.append(arr.copy()) 
                return 
            
            if t < 0: 
                return 
            
            for j in range(i, len(nums)): 
                arr.append(nums[j])
                helper(j, arr, t - nums[j]) 
                arr.pop() 
            
        helper(0, [], target)
        return res 
