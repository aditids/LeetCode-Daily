# 2402. Meeting Rooms III

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = [i for i in range(n)]
        end_times = []
        count = [0]*n
        for i,j in meetings:
            while end_times and i>=end_times[0][0]:
                k, room = heapq.heappop(end_times)
                heapq.heappush(free_rooms, room)

            if not free_rooms:
                end, room = heapq.heappop(end_times)
                j = end + j-i
                heapq.heappush(free_rooms, room)

            room=heapq.heappop(free_rooms)
            heapq.heappush(end_times,(j,room))
            count[room]+=1

        return count.index(max(count))
