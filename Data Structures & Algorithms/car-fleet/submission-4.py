class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = [] 
        for i in range(len(position)): 
            pos_sp.append((position[i], speed[i])) 
        pos_sp = sorted(pos_sp, key=lambda x: x[0], reverse=True) 

        res = [] 
        for pos, sp in pos_sp: 
            time = (target - pos) / sp 
            if res and res[-1] >= time: 
                continue 
            else: 
                res.append(time) 
        
        return len(res) 

        
        
        # pos_sp = [] 
        # for i in range(len(position)): 
        #     pos_sp.append((position[i], speed[i])) 
        # pos_sp = sorted(pos_sp, key=lambda x: x[0]) 


        # stack = [] 
        # for pos, sp in pos_sp: 
        #     miles = target - pos 
        #     time = miles / sp 
        #     while stack and stack[-1] <= time: 
        #         stack.pop() 
        #     stack.append(time) 
        
        # return len(stack) 
        
    #     stack = [] 

        
    #     res = [0] * target 
    #     for i in range(len(position)): 
    #         pos = position[i] 
    #         sp = speed[i] 
    #         miles = target - pos 
    #         time = miles / sp 
    #         res[pos] = time
        
    #     cnt = 0
    #     mx = -float("inf")
    #     for i in range(target - 1, -1, -1): 
    #         if res[i] != 0 and res[i] > mx: 
    #             cnt += 1 
    #             mx = res[i] 
    #     return cnt 
    
    # # T: O(n) 
    # # S: O(n) 