# 1043. Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            cmax = 0
            count = 0
            for j in range(i,min(len(arr),i+k)):
                cmax = max(cmax,arr[j])
                window = j-i+1
                count = max(count, dfs(j+1) + cmax * window)
            cache[i] = count
            return count
        return dfs(0)