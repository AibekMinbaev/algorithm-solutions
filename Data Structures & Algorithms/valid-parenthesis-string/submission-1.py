class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts = []
        stars = [] 

        for i in range(len(s)): 
            if s[i] == "*": 
                stars.append(i)
            elif s[i] == "(": 
                lefts.append(i) 
            elif s[i] == ")":
                if lefts: 
                    lefts.pop() 
                elif stars: 
                    stars.pop() 
                else: 
                    return False 
        
        while lefts and stars: 
            left = lefts.pop() 
            star = stars.pop() 

            if left > star: 
                return False 
        
        return not lefts 
