# 997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        total = defaultdict(int)
        for i,j in trust:
            total[i]-=1
            total[j]+=1
        for i in range(1,n+1):
            if total[i]==n-1:
                return i
        return -1
    
    # Time complexity - O(v+e)



        # if trust == [] and n==1: return 1
        # graph = {}
        # k = -1
        # for pair in trust:
        #     if pair[1] not in graph:
        #         graph[pair[1]] = []
        #     graph[pair[1]].append(pair[0])
        # for i in graph:
        #     if len(graph[i]) == n-1:
        #         k = i
        
        # for i in graph:
        #     if k in graph[i]:
        #         return -1
        # return k