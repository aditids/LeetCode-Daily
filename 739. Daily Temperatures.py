# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for w in range(len(temperatures)):
            while stack and temperatures[w]>temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = w-i
            stack.append(w)
        return result