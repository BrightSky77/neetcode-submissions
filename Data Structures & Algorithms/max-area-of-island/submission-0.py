class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c==COLS or grid[r][c] == 0 or visited[r][c] == True) :
                return False
            visited[r][c] = True
            current_area = 1
            for i in range(4):
                current_area += dfs(r+dy[i],c+dx[i])
            return current_area


        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c] == False and grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        return area
        

            

