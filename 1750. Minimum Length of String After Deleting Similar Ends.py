# 1750. Minimum Length of String After Deleting Similar Ends

class Solution:
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                while l<r and s[l]==s[l+1]:
                    l+=1
                while r>l and s[r]==s[r-1]:
                    r-=1
                l+=1
                r-=1
            else:
                return r-l+1 if r-l+1>0 else 0
        return r-l+1 if r-l+1>0 else 0