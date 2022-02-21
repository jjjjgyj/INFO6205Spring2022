# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        while node:
            res = max(res, node.val + head.val)
            node = node.next
            head = head.next
            
        return res
        
