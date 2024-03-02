# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l, r, i = 0, len(nums)-1, len(nums)-1
        while l<=r:
            if nums[l]**2>nums[r]**2:
                res[i] = nums[l]**2
                l+=1
            else:
                res[i] = nums[r]**2
                r-=1
            i-=1
        return res