class KthLargest:

    def __init__(self, k: int, nums: List[int]):  
        # TC: n log k 
        # SC: k 

        self.hp = [] 
        self.k = k 
        for num in nums: 
            heapq.heappush(self.hp, num) 
            if len(self.hp) > self.k: 
                heapq.heappop(self.hp) 

    def add(self, val: int) -> int: 
        heapq.heappush(self.hp, val) 

        while len(self.hp) > self.k: 
            heapq.heappop(self.hp) 
        return self.hp[0]
 


        
