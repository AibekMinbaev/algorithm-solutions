class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Stack solution 

        q = deque([[]])
        for num in nums:
            for _ in range(len(q)): 
                subset = q.popleft() 
                new_subset = subset.copy() 
                new_subset.append(num) 
                q.append(subset) 
                q.append(new_subset) 
        return list(q) 
