class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # First let's try this with DFS
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        visit = set()
        cycle = set()
        res = []

        def dfs(crs):    
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for nxt in graph[crs]:
                if not dfs(nxt): return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res