# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.split(head)
        
    def split(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start = slow.next
        slow.next = None
        
        l = self.split(head)
        r = self.split(start)
        
        return self.merge(l, r)
        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = curr = ListNode(None)
        while l and r:
            if l.val < r.val:
                curr.next = l 
                l = l.next 
            else:
                curr.next = r 
                r = r.next
            curr = curr.next 
        curr.next = l or r 
        
        return dummy.next
    
