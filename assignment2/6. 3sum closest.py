class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestsum = float("inf")
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closestsum - target):
                    closestsum = curr_sum
                if curr_sum - target > 0:
                    right -= 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum - target < 0:
                    left += 1 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    return curr_sum
        
        return closestsum
                    
                    
                
            
        """
        [-4,-1,1,2]
        
        1
        
        
        """
