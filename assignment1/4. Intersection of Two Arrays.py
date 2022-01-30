class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_set = set(nums1)
        nums2 = list(set(nums2))
        
        for num in nums2:
            if num in nums1_set:
                result.append(num)
        
        return result 
                
