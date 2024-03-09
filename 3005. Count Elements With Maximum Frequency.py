# 3005. Count Elements With Maximum Frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxCount = max(count.values())
        result = 0
        for freq in count.values():
            if freq==maxCount:
                result+=freq
        return result