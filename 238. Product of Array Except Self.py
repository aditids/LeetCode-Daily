# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for i in nums:
            if i==0:
                zero+=1
            else:
                product*=i
        if zero>1:
            return [0]*len(nums)
        result = []
        for i in nums:
            if zero and i==0:
                result.append(product)
            elif zero and i!=0:
                result.append(0)
            else:
                result.append(product//i)
        return result