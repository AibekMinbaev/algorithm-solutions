class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 

        n = len(heights)
        for i in range(n):
            h = heights[i] 
            w = 1 

            j = i - 1
            while j > -1 and heights[j] >= h: 
                j -= 1 
                w += 1 
            
            j = i + 1
            while j < n and heights[j] >= h: 
                j += 1 
                w += 1 
            
            res = max(res, h * w) 
        return res 



