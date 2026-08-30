class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)     #length of row (example - 3)
        n = len(matrix[0])  #length of column (example - 4)
        left = 0 
        right = m*n -1  #Getting the very last value at bottom

        while left <= right:
            mid = (left + right)//2
            row = mid // n    # row index- floor value of dividing mid / col length 
            col = mid % n     # col index- remainder of mid / col length

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False