class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] 
        for s in strs: 
            for char in s:
                if char == '1' or char == '0': 
                    res.append('0') 
                res.append(char) 
            res.append('1')
        return ''.join(res) 

    def decode(self, s: str) -> List[str]:
        res = [] 
        temp = [] 

        i = 0 
        while i < len(s): 
            char = s[i] 

            if char == '0': 
                temp.append(s[i+1])
                i += 1 
            elif char == '1': 
                res.append(''.join(temp)) 
                temp = [] 
            else:
                temp.append(char)
            i += 1  
        return res 
