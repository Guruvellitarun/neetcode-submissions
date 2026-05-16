class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        def bfs(start):
            q = collections.deque(start)
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            visit = []
            while q:
                row, col = q.popleft()
                visit.append((row, col))
                for dx, dy in directions:
                    r, c = row+dx, col+dy
                    if (0 <= r < ROWS and
                        0 <= c < COLS and
                        heights[r][c] >= heights[row][col] and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.append((r,c))
            return visit

        pacific = [(r,0) for r in range(ROWS)] + [(0,c) for c in range(COLS)]
        atlantic = [(r,COLS-1) for r in range(ROWS)] + [(ROWS-1,c) for c in range(COLS)]

        pac = bfs(pacific)
        atl = bfs(atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res