class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for idx in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (idx//3)*3 + i
                    col = (idx%3)*3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True


        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         elif board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
        
        # for col in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[j][col] == ".":
        #             continue
        #         elif board[j][col] in seen:
        #             return False
        #         seen.add(board[j][col])
        
        # for idx in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (idx//3)*3 + i
        #             #row = 0,0,0,3,3,3,6,6,6
        #             col = (idx%3)*3 + j
        #             #col = 0,3,6,0,3,6,0,3,6
        #             if board[row][col] == ".":
        #                 continue
        #             elif board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True
