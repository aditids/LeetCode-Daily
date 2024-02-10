# 368. Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # DP - 
        nums.sort()
        dp = [[i] for i in nums]
        result = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    temp = [nums[i]]+dp[j]
                    if len(temp)>len(dp[i]):
                        dp[i] = temp
            if len(dp[i])>len(result):
                result = dp[i]
        return result
        
        
        
        # Recursion -
        # nums.sort()
        # cache = {}
        # result = []

        # def dfs(i):
        #     if i==len(nums):return []
        #     if i in cache: return cache[i]
        #     r = [nums[i]]
        #     for j in range(i+1,len(nums)):
        #         if nums[j]%nums[i]==0:
        #             temp = [nums[i]] + dfs(j)
        #             if len(temp)>len(r):
        #                 r = temp
        #     cache[i] = r
        #     return r

        # for i in range(len(nums)):
        #     temp = dfs(i)
        #     if len(temp)>len(result):
        #         result = temp
              
        # return result