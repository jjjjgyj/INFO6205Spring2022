class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        int_map = Counter(nums)
        int_cnt = []
        for num, cnt in int_map.items():
            int_cnt.append([cnt, num])
            
        int_cnt.sort(key = lambda x:(x[0],-x[1]))
        
        result = []
        for cnt, num in int_cnt:
            for i in range(cnt):
                result.append(num)

        return result
