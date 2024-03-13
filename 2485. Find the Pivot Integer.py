# 2485. Find the Pivot Integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        s = (n*(n+1))//2
        k = 0
        for i in range(n,0,-1):
            k+=i
            #print(k,s,i)
            if k==s:
                return i
            s-=i
        return -1