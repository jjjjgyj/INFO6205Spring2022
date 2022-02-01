class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start, end = newInterval
        res = []
        i, length = 0, len(intervals)
        
        while i < length and start > intervals[i][0]:
            res.append(intervals[i])
            i += 1 
        
        if not res or start > res[-1][1]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], end)
        
        while i < length:
            curr_start, curr_end = intervals[i]
            if curr_start > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], curr_end)
        
            i += 1 
        
        return res 
            
