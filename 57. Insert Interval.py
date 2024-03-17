# 57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Note: It is mentioned in the question that intervals 
        # are in ascending order of their start times so we do not need to sort the array
        result = []
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:      # if new interval end time is shorter than current 
                result.append(newInterval)          # intervals start time, our new interval perfectly 
                return result+intervals[i:]         # fits into the intervals array so we return it
            elif newInterval[0]>intervals[i][1]:    # if new interval start time is greater than current
                result.append(intervals[i])         # end time, they won't overlap, we proceed to next interval
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] 
                # finally we found an overlapping interval so we just create a newInterval that would fix the current overlapping issue
        # if we still could not find a suitable position in ouur intervals array for 
        # the new interval, then the last position would be perfect for newInterval!
        result.append(newInterval)
        return result

        # Time complexity = O(n)