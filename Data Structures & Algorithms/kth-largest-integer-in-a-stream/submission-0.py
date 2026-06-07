class KthLargest:

    def __init__(self, k: int, nums: List[int]): 
        self.nums = [] 
        self.k = k 
        for num in nums: 
            heapq.heappush(self.nums, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val) 
        
        tmp = [] 
        while len(tmp) < self.k: 
            num = heapq.heappop(self.nums) 
            tmp.append(num) 
        res = -tmp[-1] 
        for num in tmp: 
            heapq.heappush(self.nums, num) 
        return res 

        
