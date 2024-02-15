# 2971. Find Polygon With the Largest Perimeter
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        i = len(nums)-1
        peri = 0
        while i>=0:            
            if total-nums[i]>nums[i] and i+1>=3:
                peri=max(peri,total)
                return peri
            total-=nums[i]
            i-=1
        return -1