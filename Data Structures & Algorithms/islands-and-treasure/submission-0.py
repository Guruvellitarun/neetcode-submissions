class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # here i am tring to use Breath First Search
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = collections.deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            row, col = q.popleft()
            for dx, dy in directions:
                r = row + dx
                c = col + dy
                if (0<= r < ROWS and
                    0<= c < COLS and
                    grid[r][c] == 2147483647
                ):
                    grid[r][c] = grid[row][col] + 1
                    q.append((r,c))
         




