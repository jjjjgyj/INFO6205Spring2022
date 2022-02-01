class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        start = 0 
        end = len(nums) - 1 
        while start < end:
            mid = (start + end) // 2 
            if (end - start) // 2 % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 2
                elif nums[mid] == nums[mid - 1]:
                    end = mid - 2 
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    end = mid - 1
                elif nums[mid] == nums[mid - 1]:
                    start = mid + 1 
                else:
                    return nums[mid]
        return nums[start]
