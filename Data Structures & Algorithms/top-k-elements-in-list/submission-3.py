class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # Bucketsort 

        freq = collections.defaultdict(int) 
        for num in nums: 
            freq[num] += 1 
        
        bucket = [[] for _ in range(len(nums)+1)] 

        for key, val in freq.items(): 
            bucket[val].append(key)

        res = [] 
        for i in range(len(bucket)-1, -1, -1): 
            if bucket[i]: 
                res += bucket[i] 
            if len(res) == k: 
                break  
        return res 


        
