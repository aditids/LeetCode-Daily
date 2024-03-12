# 791. Custom Sort String

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        hashset = Counter(s)
        for i in order:
            if i in hashset:
                res += i * hashset[i]
                hashset[i] = 0
        for i in hashset:
            res += i * hashset[i]
        return res