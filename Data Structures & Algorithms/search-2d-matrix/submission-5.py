class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1 
            while l <= r:
                middle = l + ((r - l) // 2)
                if matrix[i][middle] < target:
                    l = middle + 1
                elif matrix[i][middle] > target:
                    r = middle - 1
                else:
                    return True
        return False
