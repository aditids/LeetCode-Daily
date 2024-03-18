# 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        prev = points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>prev:
                count+=1
                prev = points[i][1]
            else:
                prev = min(prev,points[i][1])
        return count