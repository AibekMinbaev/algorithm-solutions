class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TC: n log m_k (where m_k is max elem in piles)
        # SC: 1 

        l, r = 1, max(piles) 
        while l < r: 
            k = (r + l) // 2 

            hours = 0 
            for p in piles: 
                hours += (p // k) + (1 if p % k else 0)

            if hours > h: 
                l = k + 1 
            else: 
                r = k 
        return r 

