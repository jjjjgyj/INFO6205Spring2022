class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2 
        elif not l2:
            return l1 
        
        dummy = ListNode()
        curr = dummy
        carryover = 0
        
        while l1 or l2 or carryover:
            curr.next = ListNode()
            curr = curr.next
            if not l1 and not l2:
                curr.val = carryover
                carryover = 0
            elif not l1:
                curr.val = (l2.val + carryover) % 10
                carryover = (l2.val + carryover) // 10
                l2 = l2.next   
            elif not l2:
                curr.val = (l1.val + carryover) % 10
                carryover = (l1.val + carryover) // 10
                l1 = l1.next                 
            else:  
                curr.val = (l1.val + l2.val + carryover) % 10
                carryover = (l1.val + l2.val + carryover) // 10
                l1 = l1.next 
                l2 = l2.next
        
        return dummy.next
                    
