class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star, star_close = 0, 0, 0

        for char in s: 
            if char == "(": 
                left += 1 
            elif char == "*": 
                if left: 
                    left -= 1 
                    star_close += 1 
                else: 
                    star += 1 
            elif char == ")": 
                if left: 
                    left -= 1 
                elif star_close: 
                    star_close -= 1 
                    star += 1
                elif star: 
                    star -= 1 
                else: 
                    return False 
        
        return not left 
                
                

