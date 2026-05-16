class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # let's use breath first search
        if not grid:
            return None
        
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        time = 0
  
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    visit.add((r,c))
        
        while q and visit:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in directions:
                    r, c = row+dx, col+dy
                    if (0 <= r < ROWS and 
                        0 <= c < COLS and
                        (r,c) in visit):
                        q.append((r,c))
                        visit.remove((r,c))
            time += 1    

        return time if not visit else -1