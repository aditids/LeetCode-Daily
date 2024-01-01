# 1422. Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        maxSum, zeroCount = 0, 0
        oneCount = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0': zeroCount+=1
            else : oneCount-=1
            maxSum = max(maxSum,zeroCount+oneCount)
        return maxSum
# Time Complexity - O(n)
# Space complexity - O(1)