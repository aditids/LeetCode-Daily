# 2092. Find All People With Secret

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])             # Result array
        timeList = {}                               # Adj list based on times of meetings
        for i,j,t in meetings:                      # Creating undirected graph between src, dst
            if t not in timeList:
                timeList[t] = defaultdict(list)     # Defauldict is used to prevent index out of bound for timeList[t][i/j]
            timeList[t][i].append(j)
            timeList[t][j].append(i)

        #print(timeList)
        
        def dfs(src, lst):
            if src in visited: return
            visited.add(src)
            secrets.add(src)
            for neighbor in lst[src]:               # Recursively sharing secret with all neighbors for that particular timeList[i]/lst
                #print(neighbor, lst[src])
                dfs(neighbor, lst)

        #print(sorted(timeList.keys()))

        for i in sorted(timeList.keys()):           # Now we have to iterate the timeList in sorted times, since there's a possibility of duplicate times, we've sorted timeList based on keys.
            visited = set()
            for src in timeList[i]:
                if src in secrets:                  # If src knows secrect at that particular time only then he should be allowed to share it with all the people he will be meeting at that time
                    #print(src,timeList[i])
                    dfs(src, timeList[i])

        return list(secrets)

        # time complexity - O(mlogm) -> m = meetings