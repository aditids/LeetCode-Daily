# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        k = {}
        for i in arr:
            if i in k:
                k[i]+=1
            else:
                k[i]=1

        m = set()
        for i in k.keys():
            if k[i] in m:
                return False
            else:
                m.add(k[i])
        return True
        