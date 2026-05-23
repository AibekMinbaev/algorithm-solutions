class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights) 
        res = 0 
        stack = [] 
     
        for i in range(n): 
            idx = i
            while stack and stack[-1][1] > heights[i]: 
                idx, h = stack.pop()
                area = h * (i - idx)
                res = max(res, area)
            stack.append((min(i, idx), heights[i]))

        while stack: 
            idx, h = stack.pop()
            area = h * (n - idx)
            res = max(res, area) 
        return res 
