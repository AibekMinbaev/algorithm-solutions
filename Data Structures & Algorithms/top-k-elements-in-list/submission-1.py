class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int) 

        for num in nums: 
            freq[num] += 1 

        heap = []
        for key, val in freq.items(): 
            heapq.heappush(heap, (-val, key)) 
        
        res = []
        for i in range(k): 
            val, key = heapq.heappop(heap)  
            res.append(key) 
        return res 


        # sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True) 
        # res = []
        # for i in range(k): 
        #     res.append(sorted_freq[i][0]) 
        # return res 