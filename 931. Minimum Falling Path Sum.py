# 931. Minimum Falling Path Sum
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                m = matrix[i-1][j]
                if j>0:
                    l = matrix[i-1][j-1] 
                else:
                    l = float("inf")
                if j<n-1:
                    r = matrix[i-1][j+1]
                else:
                    r = float("inf")
                matrix[i][j] += min(m,l,r)
        return min(matrix[-1])