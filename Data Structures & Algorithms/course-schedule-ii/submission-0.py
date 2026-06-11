class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        adj = {}
        for a, b in prerequisites: 
            if a not in adj: 
                adj[a] = [] 
            adj[a].append(b) 
        
        res = [] 
        taken = set()
        seen = set()
        def dfs(course: int) -> bool: 
            if course in taken: 
                return True 
            
            if course not in adj: 
                res.append(course) 
                taken.add(course) 
                return True 
           
            if course in seen: 
                return False 

            seen.add(course) 
            for prereq in adj[course]:
                if not dfs(prereq): 
                    return False 
            seen.remove(course) 
            res.append(course)
            taken.add(course) 
            return True 

        for course in range(numCourses): 
            if not dfs(course): 
                return [] 
        
        return res 

