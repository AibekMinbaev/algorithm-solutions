class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        freq = collections.Counter(t) 
        curr_freq = collections.defaultdict(int)


        def check(): 
            for k, v in freq.items(): 
                if k not in curr_freq or curr_freq[k] < v: 
                    return False 
            return True 

        res = s
        found = False 

        l = 0 
        for r in range(len(s)): 

            if s[r] in freq: 
                curr_freq[s[r]] += 1 
            
            while l <= r and (s[l] not in curr_freq or curr_freq[s[l]] > freq[s[l]]): 
                if s[l] in curr_freq: 
                    curr_freq[s[l]] -= 1 
                l +=1 
            
            if check() and r - l + 1 <= len(res): 
                found = True 
                res = s[l:r+1] 
        return res if found else ""
       