class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        # find midpoint and split list in half 
        slow, fast = head, head
        
        while fast and fast.next:
            prev1 = slow
            slow = slow.next 
            fast = fast.next.next
        
        curr = slow 
        prev1.next = None
        
        # reverse second linked list 
        prev2 = None 
        
        while curr:
            next_node = curr.next
            curr.next = prev2
            prev2 = curr
            curr = next_node
        
        # merge two linked lists
        left, right = head, prev2
        dummy, p = head, head
        while left and right:
            left_temp = left.next
            right_temp = right.next
            left.next = right
            right.next = left_temp
            left = left_temp
            p = right
            right = right_temp
            
        p.next = right
            
        return p
        
