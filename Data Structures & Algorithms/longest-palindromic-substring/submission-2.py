class Solution:
    def longestPalindrome(self, s: str) -> str: 
        # DP solution 
        # time: n^2 
        # space: n^2

        dp = [[0] * len(s) for i in range(len(s))] 

        for r in range(len(s)): 
            for c in range(r):
                dp[r][c] = 1 
        
        for r in range(len(s)-2, -1, -1): 
            for c in range(len(s)-1, -1, -1): 
                if s[r] == s[c] and dp[r+1][c-1]: 
                    dp[r][c] = 1 
        
        res = s[0]
        for r in range(len(dp)): 
            for c in range(len(dp[0])): 
                if dp[r][c] == 1 and c - r + 1 > len(res): 
                    res = s[r:c+1]
        return res 


        # # Two pointer solution 
        # # time: n^2 

        # def helper(l: int, r: int) -> str: 
        #     while l > -1 and r < len(s) and s[l] == s[r]: 
        #         l -= 1
        #         r += 1
        #     return s[l+1:r]

        # res = s[0]
        # for i in range(len(s)): 
        #     subs = helper(i, i) 
        #     if len(subs) > len(res): 
        #         res = subs 
            
        #     subs_2 = helper(i, i+1)
        #     if len(subs_2) > len(res): 
        #         res = subs_2 
        
        # return res 

