# 446. Arithmetic Slices II - Subsequence
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] += 1+dp[j][diff]
                count+=1+dp[j][diff]
        return count - (n*(n-1)//2) 