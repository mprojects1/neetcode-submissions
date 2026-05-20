class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0 
        row = len(matrix)
        col = len(matrix[0])

        r = row*col -1

        while l <= r:

            mid = (l+r)//2

            mid_row = mid // col
            mid_col = mid % col

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                r = mid -1
            else:
                l = mid+1
            
        return False