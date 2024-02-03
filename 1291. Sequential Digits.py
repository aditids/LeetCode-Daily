# 1291. Sequential Digits
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        q = [i for i in range(1,10)]
        print(q)
        while q:
            k = q.pop(0)
            if k>high: continue
            if low<=k<=high:
                result.append(k)
            temp = k%10
            if temp<9:
                q.append(k*10 + temp + 1)
        return result