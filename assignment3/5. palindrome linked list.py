class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes_val = []
        curr = head
        while curr:
            nodes_val.append(curr.val)
            curr = curr.next
            
        left = 0 
        right = len(nodes_val) - 1 
        
        while left < right:
            if nodes_val[left] != nodes_val[right]:
                return False 
            left += 1 
            right -= 1 
        
        return True
