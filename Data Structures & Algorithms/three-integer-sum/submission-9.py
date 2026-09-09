class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TC: n^2 
        # SC: 1

        nums.sort() 

        res = [] 
        for i in range(len(nums)): 
            if i > 0 and nums[i-1] == nums[i]: 
                continue 
            
            l, r = i + 1, len(nums) - 1 
            while l < r: 
                sm = nums[l] + nums[r] 

                if sm == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]]) 
                    l += 1 
                    while l < len(nums) and nums[l-1] == nums[l]: 
                        l += 1 
                    
                    r -= 1 
                    while r >= 0 and nums[r+1] == nums[r]: 
                        r -= 1 
            
                elif sm < -nums[i]: 
                    l += 1 
                else: 
                    r -= 1 
        return res 

# [-1,0,1,2,-1,-4] 

# [-4,-1,-1,0,1,2] 

# a + b + c = 0  
# a + b = -c 

