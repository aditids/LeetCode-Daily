# 2870. Minimum Number of Operations to Make Array Empty
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr = Counter(nums)
        count = 0
        for i in arr.values():
            if i == 1:
                return -1
            print(i,ceil(i/3))
            count+=ceil(i/3)
        return count