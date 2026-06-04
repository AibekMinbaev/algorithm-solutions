class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Backtracking 
        # time: 2^n * n - (at each step 2 paths, each path calls copy function) 
        # space: 2^n * n - for 2^n output list, n for curr 
        subsets = [] 

        curr = [] 
        def helper(i: int) -> None: 
            if i == len(nums): 
                subsets.append(curr.copy())
                return 

            curr.append(nums[i]) 
            helper(i+1) 
            curr.pop()
            helper(i+1)  

        helper(0) 
        return subsets 



        # # Arr solution 
        # # time: n^2 * n 
        # # space: n^2 * n 
        # subsets = [[]]
        # for num in nums:
        #     for i in range(len(subsets)): 
        #         subsets.append(subsets[i] + [num])
        # return subsets
        