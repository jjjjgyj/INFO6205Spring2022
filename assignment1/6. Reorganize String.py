class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        nums_heap = []   
        res = ""
        
        for value, count in counter.items():
            heapq.heappush(nums_heap, (-count, value))
        
        while len(nums_heap) > 1:
            count1, value1 = heapq.heappop(nums_heap)
            count2, value2 = heapq.heappop(nums_heap)
            
            res += value1
            if count1 < -1:
                heapq.heappush(nums_heap, (count1+1, value1))
                
            res += value2
            if count2 < -1:
                heapq.heappush(nums_heap, (count2+1, value2))
            
        if not nums_heap:
            return res

        count_last, value_last = heapq.heappop(nums_heap)        
        if count_last < -1:
            return ""
        else:
            return res + value_last
            

        
        
            
