# 201. Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left!=right:
            left>>=1
            right>>=1
            i+=1
        return left<<i

        # Time Complexity - O(1)
        
        # result = left
        # while left<=right:
        #     result&=left
        #     #print(result)
        #     if result == 0: return 0
        #     left+=1
        # return result

        # Time Complexity - O(n)
        