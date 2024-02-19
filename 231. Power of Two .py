# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        return n & (n-1) == 0

        # if n==1: return True
        # if n==0 or n%2!=0: return False
        # while n:
        #     if n==2: return True
        #     n=n//2
        #     if n%2!=0: return False

        # return True