class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        res = [0] * len(temperatures)
        st = [] 

        for i, n in enumerate(temperatures):
            while st and st[-1][0] < n:
                num, idx = st.pop() 
                res[idx] = i - idx
            st.append((n, i)) 
        return res 
        
        
