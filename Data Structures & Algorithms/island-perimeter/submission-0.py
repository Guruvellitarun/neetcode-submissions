class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                pram = 4
                if grid[i][j] == 0:
                    continue
                if i > 0 and grid[i-1][j] == 1: # up
                    pram -= 1
                if i < rows-1 and grid[i+1][j] == 1: # down
                    pram -= 1
                if j > 0 and grid[i][j-1] == 1: # right
                    pram -= 1
                if j < cols-1 and grid[i][j+1] == 1: # left
                    pram -= 1
                total += pram
        return total
                
