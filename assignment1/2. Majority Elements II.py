class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt_map = Counter(nums)
        res = []
        list_len = len(nums)
        for num, cnt in cnt_map.items():
            if cnt > list_len / 3:
                res.append(num)
               
        return res
