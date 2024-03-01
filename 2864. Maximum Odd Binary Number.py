# 2864. Maximum Odd Binary Number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for i in s:
            if i=='1':
                count+=1
        r = ''
        while count>1:
            count-=1
            r+='1'
        while len(r)<len(s)-1:
            r+='0'
        r+='1'
        return r