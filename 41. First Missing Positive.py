# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hmap = defaultdict(list)
        for i in nums:
            hmap[i] = 1
        pos = 1
        while True:
            if pos not in hmap:
                return pos
            pos+=1
                
        return pos