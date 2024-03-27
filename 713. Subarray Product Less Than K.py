# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        tsum = 1
        l = 0
        count = 0
        r = 0
        while r<len(nums):
            tsum*=nums[r]
            while l<r and tsum>=k:
                tsum = tsum//nums[l]
                l+=1
            if tsum<k:
                count+=r-l+1
            r+=1

        return count