# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        k = Counter(s)
        sortedK = sorted(k.items(),key=lambda x:x[1],reverse=True) # lambda function to sort chars based on their frequency in reverse order
        result = ''
        for i, j in sortedK:
            result+=i*j
        return result