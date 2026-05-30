class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        # DFS solution 
        # Detecting the cycle in the prerequitise is the key

        # time: V + E
        # space: V + E 
        
        mp = defaultdict(list) 
        for a, b in prerequisites: 
            mp[a].append(b) 

        visited: Set[int] = set()
        def dfs(course: int): 
            if course in visited: 
                return False 
            
            if course not in mp: 
                return True

            visited.add(course) 
            for p in mp[course]: 
                if not dfs(p): 
                    return False 
                    
            visited.remove(course) 
            del mp[course]
            return True

        for course in range(numCourses):
            if not dfs(course): 
                return False 
        return True 

# [0,1], [1, 2], [2, 3] 

# # 0 > 1 > 2 > 3 
