# 948. Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxScore = 0
        count = 0 
        l, r = 0, len(tokens)-1
        while l<=r :
            if power>=tokens[l]:
                print(tokens[l])
                power-=tokens[l]
                count+=1
                l+=1
                maxScore = max(maxScore, count)
            elif count>=1:
                print(tokens[r])
                power+=tokens[r]
                count-=1
                r-=1
            else:
                break
        return maxScore