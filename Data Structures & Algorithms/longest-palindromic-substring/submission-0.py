class Solution:
    def longestPalindrome(self, s: str) -> str: 

        def helper(l: int, r: int) -> str: 
            while l > -1 and r < len(s) and s[l] == s[r]: 
                l -= 1
                r += 1
            return s[l+1:r]

        res = s[0]
        for i in range(len(s)): 
            subs = helper(i, i) 
            if len(subs) > len(res): 
                res = subs 
            
            subs_2 = helper(i, i+1)
            if len(subs_2) > len(res): 
                res = subs_2 
        
        return res 

