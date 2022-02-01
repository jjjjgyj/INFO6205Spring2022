class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1 
        
        pq = []
        for x, y in num_count.items():
            heapq.heappush(pq, (-y, x))
        
        res = []
        for _ in range(k):
            count, value = heapq.heappop(pq)
            res.append(value)
        
        return res
            
 
