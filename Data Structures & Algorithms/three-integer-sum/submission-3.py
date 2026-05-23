class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = set()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1 
            target = -nums[i]
            while l < r: 
                if nums[l] + nums[r] == target:
                    triple = sorted([nums[i], nums[l], nums[r]]) 
                    res.add(tuple(triple))
                    l += 1 
                    r -= 1
                elif nums[l] + nums[r] < target: 
                    l += 1 
                else: 
                    r -= 1  
        return [list(triple) for triple in res ] 

        # # Brute force 
        # # time: n^3
        # # space: n
        # res = set() 
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         for k in range(j+1, len(nums)): 
        #             if nums[i] + nums[j] + nums[k] == 0: 
        #                 res.add(tuple(sorted([nums[i], nums[j], nums[k]]))) 
        # return [list(t) for t in res] 

