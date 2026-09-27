class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dy = [-1,1,0,0]
        dx = [0,0,1,-1]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i,j):
            if (i < 0 or j < 0 or (i >= len(grid)) or (j >= len(grid[0]) or grid[i][j] == "0" or visited[i][j] == True )):
                return
            visited[i][j] = True
            for k in range(4):
                dfs(i+dx[k],j+dy[k])

        cnt = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(i,j)
                    cnt += 1
        return cnt


