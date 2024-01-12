# 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        vowels = ['a','e','i','o','u']
        j = len(s)//2
        a, b = 0, 0
        for i in range(n//2):
            if s[i] in vowels:
                a+=1
            if s[j] in vowels:
                b+=1        
            j+=1
        return a==b  
    # Time Complexity - O(n)      