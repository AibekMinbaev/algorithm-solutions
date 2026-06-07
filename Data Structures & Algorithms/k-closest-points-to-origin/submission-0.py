class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        hp = [] 

        for x, y in points: 
            d = math.sqrt((x - 0)**2 + (y - 0)**2) 
            heapq.heappush(hp, (d, (x,y))) 
        
        res = [] 
        for i in range(k): 
            d, (x,y) = heapq.heappop(hp) 
            res.append([x,y]) 
        return res 

