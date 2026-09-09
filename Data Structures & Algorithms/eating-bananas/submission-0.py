class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TC: n log m_k (where m_k is max elem in piles)
        # SC: 1 

        def get_hours(k: int) -> int: 
            hours = 0 
            for p in piles: 
                hours += p // k 
                hours += 1 if p % k else 0 
            return hours 

        l, r = 1, max(piles) 
        while l < r: 
            k = (r + l) // 2 
            hours = get_hours(k) 

            if hours > h: 
                l = k + 1 
            else: 
                r = k 
        return r 

