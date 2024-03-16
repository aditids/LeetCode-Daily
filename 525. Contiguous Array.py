# 525. Contiguous Array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        hashtable = {0:-1}
        count = 0

        for i, num in enumerate(nums):
            if num==0:
                prefix_sum+=1
            else:
                prefix_sum-=1
            if prefix_sum in hashtable:
                count = max(count, i-hashtable[prefix_sum])
            else:
                hashtable[prefix_sum] = i
        
        return count