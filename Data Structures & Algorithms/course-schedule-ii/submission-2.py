class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # First let's try this with DFS
        graph = {i:[] for i in range(numCourses)}
        res = []
        visited, cycle = set(), set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)    

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            res.append(node)
            visited.add(node)
            cycle.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res