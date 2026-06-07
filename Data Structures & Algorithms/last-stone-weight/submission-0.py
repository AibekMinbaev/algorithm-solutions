class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # time: n * logn
        # space: n 
        hp = [] 

        for stone in stones: 
            heapq.heappush(hp, -stone) 

        while len(hp) > 1: 
            stone_a = -heapq.heappop(hp) 
            stone_b = -heapq.heappop(hp) 
            if stone_a != stone_b: 
                stone_c = max(stone_a, stone_b) - min(stone_a, stone_b) 
                heapq.heappush(hp, -stone_c) 
        
        if not hp: 
            return 0 
        return -hp[0] 