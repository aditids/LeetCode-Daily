# 2125. Number of Laser Beams in a Bank
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        count = 0
        for row in bank:
            rc = row.count('1')
            print(rc)
            if prev == 0 and rc!=0:
                prev = rc
            elif rc!=0:
                count = count+(prev*rc)
                prev = rc
        return count
        # Time complexity - O(n)
        # Space Complexity - O(1)