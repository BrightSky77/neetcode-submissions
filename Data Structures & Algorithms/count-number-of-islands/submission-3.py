from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dy = [-1,1,0,0]
        dx = [0,0,1,-1]
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def bfs(i,j):
            grid[i][j] == "0"
            q = deque([(i,j)])

            while q:
                row,col = q.popleft()
                for k in range(4):
                    ny = row + dy[k]
                    nx = col + dx[k]
                    if (0<=ny<m) and (0<=nx<n) and grid[ny][nx] == "1":
                        grid[ny][nx] = "0"
                        q.append((ny,nx))

      
        # def dfs(i,j):
        #     grid[i][j] = "0"
        #     for k in range(4):
        #         ny = i +dy[k]
        #         nx = j + dx[k]
        #         if (0<=ny<m) and (0<=nx<n) and grid[ny][nx] == "1":
        #             dfs(ny,nx)
        


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    ans += 1
        return ans




