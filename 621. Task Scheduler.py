# 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ht = Counter(tasks)
        maxheap = []
        for i in ht:
            heapq.heappush(maxheap,-ht[i])
        heapq.heapify(maxheap)
        time = 0
        q = []
        
        while q or maxheap:
            time+=1
            if maxheap:
                k = heapq.heappop(maxheap)
                k+=1
                if k:
                    q.append([k,time+n])
            if q and q[0][1] == time:
                k = q.pop(0)
                heapq.heappush(maxheap,k[0])
       
        return time
    
    # Time complexity - O(n)