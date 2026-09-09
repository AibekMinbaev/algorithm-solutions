class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs: 
            hash = [0] * 26 
            for ch in s: 
                idx = ord(ch) - ord('a') 
                hash[idx] += 1 

            hash = str(hash) 
            if hash not in group: 
                group[hash] = [] 

            group[hash].append(s) 

        return list(group.values())

            