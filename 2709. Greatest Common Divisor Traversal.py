# 2709. Greatest Common Divisor Traversal

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        nums = set(nums)
        if 1 in nums:return False
        if len(nums)==1:return True
        
        self.count = len(nums)
        self.parent = [i for i in range(len(nums))]
        self.size = [1]*len(nums)

        def findConn(i):
            if self.parent[i]!=i:
                self.parent[i] = findConn(self.parent[i])
            return self.parent[i]
        
        def union(i,j):
            pi, pj= findConn(i), findConn(j)
            if pi==pj: return
            if self.size[pi]<self.size[pj]:
                self.parent[pi] = pj
                self.size[pj] = self.size[pi]
            else:
                self.parent[pj] = pi
                self.size[pi] = self.size[pj]
            self.count-=1

        factorList = defaultdict(int)
        for i,n in enumerate(nums):
            f = 2
            while f*f<=n:
                if n%f==0:
                    if f in factorList:
                        union(i,factorList[f])
                    else:
                        factorList[f] = i
                    while n%f==0:
                        n=n//f
                f+=1
            if n>1:
                if n in factorList:
                    union(i, factorList[n])
                else:
                    factorList[n] = i
        
        return self.count == 1