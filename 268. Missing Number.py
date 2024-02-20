# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        return total-sum(nums)

# Time Complexity - O(n)
# Space Complexity - O(1)