from collections import deque
from copy import deepcopy
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        dy = [-1,1,0,0]
        dx = [0,0,-1,1]

        if m == 1 and n==1 :
            return

        def bfs(row,col,board):
            board_rst = deepcopy(board)
            q = deque([(row,col)])
            loop = True
            board_rst[row][col] = "X"
            while q:
                y,x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if (ny == 0 or ny == m-1 or nx ==0 or nx == n-1) and (0<=ny<m) and (0<=nx<n) and board_rst[ny][nx] == "O":
                        loop = False 
                        break
                    elif (0<ny<m-1) and (0<nx<n-1) and board_rst[ny][nx] == "O":
                        board_rst[ny][nx] = "X"
                        q.append((ny,nx))
                    
                if not loop:
                    return board
            return board_rst

        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == "O":
                    board[:] = bfs(i,j,board)

        

    
            

        
                


    
    