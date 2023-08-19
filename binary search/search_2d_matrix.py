class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        h = rows - 1

        while(l < h):
            
            m = (l+h)//2 + 1

            if target < matrix[m][0]:
                h = m - 1
            elif target > matrix[m][0]:
                l = m
            else:
                return True

        i = l
        if matrix[i][0] == target:
            return True 

        l = 0
        h = columns - 1

        while(l < h):
            
            m = (l+h)//2

            if target < matrix[i][m]:
                h = m - 1
            elif target > matrix[i][m]:
                l = m + 1
            else:
                return True

        if matrix[i][l] == target:
            return True 

        return False