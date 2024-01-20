# 907. Sum of Subarray Minimums

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        result = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []
        for i, j in enumerate(arr):
            while stack and j<stack[-1][1]:
                n,m = stack.pop()
                l = n-stack[-1][0] if stack else n+1
                r = i-n
                result = (result+m*l*r)% mod
            stack.append((i,j))
        return result

        