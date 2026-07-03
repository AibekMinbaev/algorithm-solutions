class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): 
            return False 

        s1_freq, s2_freq = [0] * 26, [0] * 26 
        for i in range(len(s1)): 
            s1_freq[ord(s1[i]) - ord('a')] += 1 
            s2_freq[ord(s2[i]) - ord('a')] += 1 

        
        if s1_freq == s2_freq: 
            return True 

        l = 0
        for r in range(len(s1), len(s2)):  
            s2_freq[ord(s2[r]) - ord('a')] += 1 
            s2_freq[ord(s2[l]) - ord('a')] -= 1 
                  
            if s1_freq == s2_freq: 
                return True  
            l += 1 

        return False 







        # if len(s2) < len(s1): 
        #     return False 

        # freq = {} 
        # for ch in s1: 
        #     if ch not in freq: 
        #         freq[ch] = 0 
        #     freq[ch] += 1

        # l, r = 0, 0
        # while r < len(s2):

        #     if s2[r] not in freq: 
        #         while l <= r: 
        #             if s2[l] in freq: 
        #                 freq[s2[l]] += 1 
        #             l += 1 
        #     else: 
        #         while not freq[s2[r]]: 
        #             freq[s2[l]] += 1
        #             l += 1 
        #         freq[s2[r]] -= 1 
        #         if r - l + 1 == len(s1): 
        #             return True 
        #     r += 1 
        # return False 

            
