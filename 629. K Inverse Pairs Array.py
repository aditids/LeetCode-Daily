# 629. K Inverse Pairs Array
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1  
        for N in range(1,n+1):
            cur = [0]*(k+1)
            count = 0
            for K in range(0,k+1):
                if K>=N:
                    count-=dp[K-N]
                count = (count+dp[K]) % mod
                cur[K] = count
            dp = cur
        return dp[k]