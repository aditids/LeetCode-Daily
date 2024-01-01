# 455. Assign Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j, count = 0, 0, 0
        g.sort()
        s.sort()
        while j<len(s) and i<len(g):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1

        return count
        # Time complexity - O(nlogn)
        # Space complexity - O(1)