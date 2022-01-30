class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        red_ind = 0 
        blue_ind = len(nums) - 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[red_ind] = nums[red_ind], nums[i]
                red_ind += 1 
        
        for j in range(len(nums) - 1, red_ind - 1, -1):
            if nums[j] == 2:
                nums[j], nums[blue_ind] = nums[blue_ind], nums[j]
                blue_ind -= 1 
                
        
