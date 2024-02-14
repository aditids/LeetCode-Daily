# 2108. Find First Palindromic String in the Array

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[0]==word[len(word)-1]:
                i=0
                j=len(word)-1
                while i<=j:
                    if word[i]!=word[j]:
                        break
                    i+=1
                    j-=1
                if i>=j:
                    return word
        return ""