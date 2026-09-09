class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TC: n 
        # SC: n 
        
        res = [0] * len(temperatures) 

        mx_tmp_idx = [] 

        for i in range(len(temperatures)-1, -1, -1): 
            while mx_tmp_idx and temperatures[mx_tmp_idx[-1]] <= temperatures[i]: 
                mx_tmp_idx.pop() 
            
            if mx_tmp_idx: 
                res[i] = mx_tmp_idx[-1] - i 
            mx_tmp_idx.append(i) 
        return res 

            