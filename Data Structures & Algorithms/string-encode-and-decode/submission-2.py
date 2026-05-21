class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = ""
        for s in strs: 
            s_encoded = str(len(s)) + "#" + s 
            res += s_encoded
        return res 

    def decode(self, s: str) -> List[str]: 
        res = [] 

        i = 0 
        while i < len(s): 
            ln = "" 
            while s[i] != "#": 
                ln += s[i] 
                i += 1 
            i += 1 
            curr = [] 
            for j in range(i, i + int(ln)): 
                curr.append(s[j]) 
                i += 1 
            res.append("".join(curr)) 
        return res 






            
 