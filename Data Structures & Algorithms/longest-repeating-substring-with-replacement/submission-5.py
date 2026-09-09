class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Sliding Window 
        # time: O(n) 
        # space: 26 

        res = 0 
        freq = {} 
       
        l, r = 0, 0 
        while r < len(s): 
            if s[r] not in freq: 
                freq[s[r]] = 0 
            freq[s[r]] += 1 

            flip = (r - l + 1) - max(freq.values())
            while l < r and flip > k: 
                freq[s[l]] -= 1 
                l += 1
                flip = (r - l + 1) - max(freq.values())
            
            res = max(res, r - l + 1)
            r += 1 

        return res 

        
        # # Brute Force: 
        # # time: n^3 
        # # space: n
        
        # res = 0 
        # for i in range(len(s)): 
        #     for j in range(i, len(s)): 
        #         sub_str = s[i:j+1] 
        #         freq = collections.Counter(sub_str)
        #         res = max(res, max(freq.values())) 
        
        # return min(len(s), res + k) 