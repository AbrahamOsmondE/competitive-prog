# Edge case hell 😭
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        n = len(matrix[0])
        m = len(matrix)

        j = 0
        i = 0

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            lower_bound = matrix[i][0]
            upper_bound = matrix[i][-1]
            if lower_bound <= target and upper_bound >= target:
                break
            elif lower_bound >= target:
                right = i - 1
            else:
                left = i + 1
        
        left = 0
        right = n
        if target < matrix[i][0] or target > matrix[i][-1]:
            return False
        while left <= right:
            j = (left + right) // 2
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = j + 1
            else:
                right = j - 1
        
        return False
        