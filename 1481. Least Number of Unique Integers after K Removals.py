# 1481. Least Number of Unique Integers after K Removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        scount = sorted(count.items(), key=lambda x: x[1])
        for i, f in scount:            
            if k>=f:
                k-=f
                del count[i]
            else:
                break
            
        return len(count)