class Solution:
    def countBits(self, n: int) -> List[int]: 
        res = [] 
        for i in range(n+1): 
            cnt = 0
            for j in range(32): 
                mask = 1 << j 
                if mask & i: 
                    cnt += 1 
            res.append(cnt) 
        return res 