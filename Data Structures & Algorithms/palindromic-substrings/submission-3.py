class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP solution 
        # time: n^2 
        # space: n^2  
        n = len(s) 
        dp = [[False] * n for _ in range(n)] 

        for r in range(n): 
            for c in range(r+1): 
                dp[r][c] = True 
            
        for r in range(n - 2, -1, -1): 
            for c in range(n - 1, -1, -1): 
                if s[r] == s[c] and dp[r+1][c-1]: 
                    dp[r][c] = True 
        
        cnt = 0 
        for r in range(n): 
            for c in range(r, len(s)): 
                if dp[r][c]: 
                    cnt += 1 
        return cnt 


        # # Two pointer solution 
        # # time: n^2 
        # # space: 1

        # def helper(l: int, r: int) -> int: 
        #     cnt = 0 
        #     while l > -1 and r < len(s) and s[l] == s[r]: 
        #         cnt += 1
        #         l -= 1 
        #         r += 1 
        #     return cnt  

        # res = 0 
        # for i in range(len(s)): 
        #     res += helper(i, i) 
        #     res += helper(i, i+1)
        # return res 
