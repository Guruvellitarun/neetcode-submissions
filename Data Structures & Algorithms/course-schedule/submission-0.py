class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first we will try to do with bfs
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        q = collections.deque()
        complete = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            complete += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return numCourses == complete