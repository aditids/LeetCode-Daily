#387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = Counter(s)
        for i in range(len(s)):
            if k[s[i]]==1:
                return i
        print(k)
        return -1