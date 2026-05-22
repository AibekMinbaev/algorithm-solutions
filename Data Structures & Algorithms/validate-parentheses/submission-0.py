class Solution:
    def isValid(self, s: str) -> bool: 
        brs = {"(": ")", "{": "}", "[":"]"}
        
        stack = [] 
        for br in s: 
            if br in brs: 
                stack.append(br) 
            else: 
                if not stack: 
                    return False 
                    
                br_right = stack.pop() 
                if brs[br_right] != br: 
                    return False 
        
        return not stack



            
