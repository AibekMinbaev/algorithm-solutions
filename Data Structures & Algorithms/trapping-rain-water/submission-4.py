class Solution:
    def trap(self, height: List[int]) -> int: 
        n = len(height) 

        mx_left = [0] * n
        for i in range(n): 
            if i == 0: 
                mx_left[i] = height[i] 
            else: 
                mx_left[i] = max(mx_left[i-1], height[i]) 
        
        mx_right = [0] * n
        for i in range(n - 1, -1, -1): 
            if i == n - 1: 
                mx_right[i] = height[i] 
            else: 
                mx_right[i] = max(mx_right[i+1], height[i]) 
        
        res = 0 
        for i in range(1, len(height) - 1): 
            p = min(mx_left[i-1], mx_right[i+1]) - height[i]
            res += max(0, p) 
        return res 
        
