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

            prereqs = mp[course]
            seen.add(course) 
            for p in prereqs: 
                if not dfs(p, seen.copy()): 
                    return False
            return True

        for course in mp.keys(): 
            if not dfs(course, set()): 
                return False 
        return True 
