# 930. Binary Subarrays With Sum

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # More optimized version - 
        
        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        tsum = 0
        
        for i in nums:
            tsum += i
            count += prefix_sum[tsum - goal]
            prefix_sum[tsum] += 1
        
        return count


        # l = r = tsum = count = 0
        # while r<len(nums):            
        #     tsum+=nums[r]
        #     while tsum>goal and l<r:
        #         tsum-=nums[l]
        #         l+=1           
        #     if tsum==goal:
        #         count+=1
        #         temp = l
        #         while nums[temp]==0 and temp<r:
        #             count+=1
        #             temp+=1            
        #     r+=1           
        # return count