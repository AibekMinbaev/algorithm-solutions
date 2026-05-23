class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = [0] * target 
        for i in range(len(position)): 
            pos = position[i] 
            sp = speed[i] 
            miles = target - pos 
            time = miles / sp 
            res[pos] = time
        
        cnt = 0
        mx = -float("inf")
        for i in range(target - 1, -1, -1): 
            if res[i] != 0 and res[i] > mx: 
                cnt += 1 
                mx = res[i] 
        return cnt 