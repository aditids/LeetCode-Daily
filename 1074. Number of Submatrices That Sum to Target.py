# 1074. Number of Submatrices That Sum to Target
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        msum = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                top = msum[r-1][c] if r>0 else 0
                left = msum[r][c-1] if c>0 else 0
                tleft = msum[r-1][c-1] if r>0 and c>0 else 0
                msum[r][c] = matrix[r][c]+top+left-tleft
        
        result = 0
        for r in range(m):
            for i in range(r, m):
                count = defaultdict(int)
                count[0] = 1
                for c in range(n):
                    cur = msum[i][c]-(msum[r-1][c] if r>0 else 0)
                    diff = cur - target
                    result+=count[diff]
                    count[cur]+=1
        return result