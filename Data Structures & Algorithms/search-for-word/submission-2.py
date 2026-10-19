class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        def dfs(i,j,idx):

            if idx == len(word):
                return True
            

            if not((0<=i<row) and (0<=j<col)) or (board[i][j] not in word[idx]) or visited[i][j] == True:
                return False

            visited[i][j] = True
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)
            visited[i][j] = False
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False
