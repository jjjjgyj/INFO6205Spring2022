class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        origin = self.binary_search(arr, k, x)
        res = [arr[origin]]
        left, right = origin - 1, origin + 1
        for i in range(k-1):
            if self.is_left_closer(arr, x, left, right):
                res.append(arr[left])
                left -= 1 
            else:
                res.append(arr[right])
                right += 1 
            
        return sorted(res) 
        
    def binary_search(self, arr, k, x):
        start = 0 
        end = len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2 
            if arr[mid] < x:
                start = mid 
            elif arr[mid] > x:
                end = mid 
            else:
                return mid 
    
        if x - arr[start] <= arr[end] - x:
            return start 
        else:
            return end 
    
    def is_left_closer(self, arr, x, left, right):
        if left < 0:
            return False
        if right > len(arr) - 1:
            return True 
        if x - arr[left] <= arr[right] - x:
            return True 
         
        
    
