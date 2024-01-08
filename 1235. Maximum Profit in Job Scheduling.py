# 1235. Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        table = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(table): return 0
            if i in cache : return cache[i]

            maxProfit = dfs(i+1)

            j = bisect.bisect(table, (table[i][1], -1, -1))
            cache[i] = maxProfit = max(maxProfit, table[i][2]+dfs(j))
            return maxProfit
        return dfs(0)