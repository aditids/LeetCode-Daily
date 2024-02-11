# 1463. Cherry Pickup II

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        cache = {}

        def dfs(r,c1,c2):
            if (r,c1,c2) in cache: return cache[(r,c1,c2)]
            if c1==c2 or c1<0 or c2<0 or c1>=n or c2>=n: return 0
            if r==m-1: return grid[r][c1]+grid[r][c2]
            
            result = 0
            maxRange = [-1,0,1]
            for i in maxRange:
                for j in maxRange:
                    result = max(result, dfs(r+1, c1+maxRange[i], c2+maxRange[j]))
            
            cache[(r,c1,c2)] = result + grid[r][c1] + grid[r][c2]
            return cache[(r,c1,c2)]

        return dfs(0,0,n-1)