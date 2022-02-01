class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] < target:
                left = mid 
            elif nums[mid] > target:
                right = mid 
            else:
                return mid 
        
        if nums[right] < target:
            return right + 1 
        elif nums[left] < target:
            return left + 1 
        else:
            return left
