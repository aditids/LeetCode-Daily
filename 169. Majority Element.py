# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        c = 0
        for i in nums:
            if c==0:
                result = i
            if result == i:
                c+=1
            else:
                c-=1
        return result

        # count = {}
        # for i in nums:
        #     if i in count:
        #         count[i] = count[i]+1
        #     else:
        #         count[i] = 1
        # print(count)
        # for i,j in count.items():
        #     if j > len(nums)//2:
        #         return i