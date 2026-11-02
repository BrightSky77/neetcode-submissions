class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        n = len(word)
        dy = [-1,1,0,0]
        dx = [0,0,1,-1]
        visited = [[False] * col for _ in range(row)]


        def dfs(i,j,depth):
            if depth == n-1:
                return True
            visited[i][j] = True
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if (0<=ny<row) and (0<=nx<col) and (board[ny][nx] == word[depth+1]) and not visited[ny][nx] :
                    bool_res = dfs(ny,nx,depth+1)
                    if bool_res:
                        return True 
            visited[i][j] = False 
            return False


        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    boolean = dfs(i,j,0)
                    if boolean:
                        return True
        return False