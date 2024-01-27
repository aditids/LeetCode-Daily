# 576. Out of Boundary Paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 +7
        dp = {}
        def dfs(r,c,moves):
            if (r<0 or r==m or c<0 or c==n):
                return 1
            if moves == 0:
                return 0
            if (r, c, moves) in dp:
                return dp[(r, c, moves)]
            dp[(r, c, moves)] = ((dfs(r+1, c, moves-1) + dfs(r-1, c, moves-1)) % mod + (dfs(r, c+1, moves-1) + dfs(r, c-1, moves-1)) % mod) % mod
            return dp[(r, c, moves)]
        return dfs(startRow, startColumn, maxMove)