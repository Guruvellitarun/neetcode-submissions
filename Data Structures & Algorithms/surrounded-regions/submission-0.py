class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visit = []

        # let add the boundray "O" to the queue
        for r in range(ROWS):
            for c in [0,COLS-1]:
                if board[r][c] == "O":
                    q.append((r,c))
        for c in range(COLS):
            for r in [0, ROWS-1]:
                if board[r][c] == "O":
                    q.append((r,c))
        
        while q:
            row, col = q.popleft()
            if board[row][col] == "O":
                board[row][col] = "T"
            visit.append((row, col))
            for dx, dy in directions:
                r, c = row+dx, col+dy
                if (0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] == "O" and
                    (r,c) not in visit):
                    q.append((r,c))
                    visit.append((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"