# 1239. Maximum Length of a Concatenated String with Unique Characters
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        hset = set()
        def isUnique(hset, s):
            k = Counter(hset) + Counter(s)
            return max(k.values())>1
        def bt(i):
            if i == len(arr): return len(hset)
            k = 0
            if not isUnique(hset, arr[i]):
                for j in arr[i]:
                    hset.add(j)
                k = bt(i+1)
                for j in arr[i]:
                    hset.remove(j)
            return max(k,bt(i+1))
        return bt(0)        