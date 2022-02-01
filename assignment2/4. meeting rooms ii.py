class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])      
        rooms = []
        for interval in intervals:
            if not rooms:
                heappush(rooms, interval[1])
                continue 
            if interval[0] < rooms[0]:
                heappush(rooms, interval[1])
            else:
                heapreplace(rooms, interval[1])
        return len(rooms)
