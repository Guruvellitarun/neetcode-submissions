class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        visit = set()
        
        for i in range(ROWS):
            for j in [0,COLS-1]:
                if board[i][j] == "O":
                    q.append((i, j))
                    board[i][j] = "T"
        for i in [0, ROWS-1]:
            for j in range(COLS):
                if board[i][j] == "O":
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            board[row][col] = "T"
            for dx, dy in directions:
                r, c = row+dx, col+dy
                if (0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] == "O" and
                    (r,c) not in visit):
                    visit.add((r,c))
                    q.append((r,c))
                    board[r][c] = "T"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
