class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Stack solution 

        stack = [[]] 
        for num in nums:
            new_stack = [] 
            while stack: 
                subset = stack.pop() 
                new_subset = subset.copy() 
                new_subset.append(num) 
                new_stack.append(subset) 
                new_stack.append(new_subset) 
            stack = new_stack 
        return stack 
