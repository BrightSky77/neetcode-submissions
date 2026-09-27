class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if (r<0 or c<0 or r>=ROWS or c>=COLS or word[i] != board[r][c] or visited[r][c]):
                return False
            
            res = False
            visited[r][c] = True
            for k in range(4):
                if dfs(r+dy[k],c+dx[k],i+1):
                    res = True
                    break
            visited[r][c] = False
            return res
            


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False