# 2610. Convert an Array Into a 2D Array With Conditions
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []       
        n = 0
        while n<len(nums):
            hasht = set()
            for i in range(len(nums)):
                if nums[i]!=0 and nums[i] not in hasht:
                    hasht.add(nums[i])
                    n+=1
                    nums[i] = 0
            print(nums)
            result.append(hasht)
        return result

    # Time and Space Complexity - O(n^2)