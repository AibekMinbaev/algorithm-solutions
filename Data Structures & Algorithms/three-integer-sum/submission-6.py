class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: 
                continue 

            l, r = i+1, len(nums) - 1 
            target = -nums[i]
            
            while l < r: 
                if nums[l] + nums[r] == target:
                    triple = [nums[i], nums[l], nums[r]]
                    res.append(triple)
                    l += 1 
                    r -= 1

                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
                    
                    while l < r and nums[r] == nums[r+1]: 
                        r -= 1
                 
                elif nums[l] + nums[r] < target: 
                    l += 1 
                else: 
                    r -= 1  
        return res

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
