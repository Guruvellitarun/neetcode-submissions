class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # here we are going to check if the tree contaion a cycle or not
        graph = {i:[] for i in range(n)}
        visit = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nxt in graph[node]:
                if nxt == prev:
                    continue
                if not dfs(nxt, node):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visit)