class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        # Arr solution 
        # time: n^2 * n 
        # space: n^2 * n 
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)): 
                subsets.append(subsets[i] + [num])
        return subsets 
