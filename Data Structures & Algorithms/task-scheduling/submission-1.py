class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.defaultdict(int) 
        for t in tasks: 
            freq[t] += 1 
        
        heap = [] 
        for val in freq.values(): 
            heapq.heappush(heap, -val)

        cycle = 0
        q = deque([]) 
        while heap or q: 
            cycle += 1 
            if q and cycle - q[0][1] - 1 >= n: 
                freq, prev_cycle = q.popleft() 
                heapq.heappush(heap, freq) 
            
            if heap: 
                freq = heapq.heappop(heap) 
                if abs(freq) - 1 > 0: 
                    q.append((-(abs(freq) - 1), cycle)) 
        return cycle 



