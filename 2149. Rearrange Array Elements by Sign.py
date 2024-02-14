# 2149. Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i=0
        j=1
        for n in nums:
            if n>0:
                result[i] = n
                i+=2
            else:
                result[j] = n
                j+=2
        return result