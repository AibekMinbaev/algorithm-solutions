class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        mp = defaultdict(list) 
        for a, b in prerequisites: 
            mp[a].append(b) 

        def dfs(course: int, seen: Set[int]): 
            if course in seen: 
                return False 
            
            if course not in mp: 
                return True

            seen.add(course) 
            for p in mp[course]: 
                if not dfs(p, seen.copy()): 
                    return False 
            
            del mp[course]
            return True

        for course in range(numCourses):
            if not dfs(course, set()): 
                return False 
        return True 
