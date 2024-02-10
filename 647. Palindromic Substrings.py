# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        def checkPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                self.count+=1
                r+=1
                l-=1

        for i in range(len(s)):
            checkPalindrome(i,i)
            checkPalindrome(i,i+1)

        return self.count
    
    # Time Complexity - O(n^2)