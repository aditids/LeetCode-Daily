# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        while n-1:
            temp = a
            a = a+b
            b = temp
            n-=1
        return a