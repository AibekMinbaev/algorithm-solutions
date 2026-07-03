class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): 
            return False 

        s1_freq, s2_freq = [0] * 26, [0] * 26 
        for i in range(len(s1)): 
            s1_freq[ord(s1[i]) - ord('a')] += 1 
            s2_freq[ord(s2[i]) - ord('a')] += 1 

        matches = 0 
        for i in range(26): 
            matches += (1 if s1_freq[i] == s2_freq[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):  
            if matches == 26: 
                return True 
            
            idx = ord(s2[r]) - ord('a')
            if s1_freq[idx] == s2_freq[idx]: 
                matches -= 1

            s2_freq[idx] += 1 
            if s1_freq[idx] == s2_freq[idx]: 
                matches += 1 

            idx = ord(s2[l]) - ord('a')
            if s1_freq[idx] == s2_freq[idx]: 
                matches -= 1
                 
            s2_freq[idx] -= 1 
            if s1_freq[idx] == s2_freq[idx]: 
                matches += 1 
            l += 1 

        return matches == 26 







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

            
