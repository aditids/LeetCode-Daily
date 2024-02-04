# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or len(t)==0:
            return ""
        l = 0
        r = 0
        minCount = 1000000
        curWindow = {}
        tCount = {}
        for i in t:
            tCount[i] = 1+tCount.get(i,0)
        a,b = 0,len(tCount)
        l = 0 
        minWS = [-1,-1]
        for r in range(len(s)):
            k = s[r]
            curWindow[k] = 1+curWindow.get(k,0)
            if k in tCount and curWindow[k]==tCount[k]:
                a+=1
            while a==b:
                if r-l+1 < minCount:
                    minWS = [l,r]
                    minCount = r-l+1
                curWindow[s[l]]-=1
                if s[l] in tCount and curWindow[s[l]]<tCount[s[l]]:
                    a-=1
                l+=1
        l,r = minWS
        return s[l:r+1] if minCount < 1000000 else ""
