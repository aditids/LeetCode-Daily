# 645. Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0]*(len(nums)+1)
        result = []
        for i in nums:
            if arr[i]==0:
                arr[i] = i
            else:
                result.append(i)
        for i in range(1,len(arr)):
            if arr[i]==0:
                result.append(i)
        return result