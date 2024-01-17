# 2225. Find Players With Zero or One Losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        for match in matches:
            if match[0] in winners:
                winners[match[0]]+=1
            elif match[0] not in losers:
                winners[match[0]] = 1
            if match[1] in winners:
                del winners[match[1]]
            if match[1] in losers:
                losers[match[1]]+=1
            elif match[1] not in losers:
                losers[match[1]] = 1

        print(winners)
        print(losers)
        w = [i for i in winners.keys()]
        l = [i for i, count in losers.items() if count == 1]
        

        print(w)
        print(l)
        w.sort()
        l.sort()
        return [w,l]