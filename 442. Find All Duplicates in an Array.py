# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:        
        res = []
        for i in nums:
            k = abs(i)-1
            if nums[k]<0:
                res.append(k+1)
            else:
                nums[k]*=-1
        return res

        # Time complexity - O(n)
        # Space complexity - O(1)