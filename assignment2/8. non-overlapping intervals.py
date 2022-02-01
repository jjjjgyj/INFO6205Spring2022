class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlapping = 0 
        intervals.sort(key = lambda x:x[1])
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                overlapping += 1 
            else:
                last_end = intervals[i][1]
        
        return overlapping
