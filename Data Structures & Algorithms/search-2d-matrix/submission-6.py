class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        bottom, top = 0, row-1

        while bottom <= top:
            mid = (top+bottom)//2
            if matrix[mid][0] > target:
                top = mid-1
            elif matrix[mid][-1] < target:
                bottom = mid+1
            else:
                break
        
        selected_row = (bottom+top)//2

        l,r = 0,col-1

        while l <= r:
            mid_col = (l+r)//2
            if matrix[selected_row][mid_col] < target:
                l = mid_col+1
            elif matrix[selected_row][mid_col] > target:
                r = mid_col - 1
            else:
                return True

        return False 