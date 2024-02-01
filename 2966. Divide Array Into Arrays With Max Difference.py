#2966. Divide Array Into Arrays With Max Difference 
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i<len(nums):
            x,j = 0,i+1
            
            if nums[i]==-1:
                i+=1
            else:
                temp = []
                while j<len(nums) and x<2:
                    if nums[j]!=-1 and nums[j]-nums[i]<=k:
                        temp.append(nums[j])
                        nums[j]=-1
                        
                        x+=1
                    j+=1
                temp.append(nums[i])
                print(temp)
                if len(temp)==3:
                    nums[i]=-1
                    result.append(temp)
                    i+=1
                else:
                    return []
        return result