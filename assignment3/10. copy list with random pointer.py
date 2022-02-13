class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        curr1 = head 
        while curr1:
            copy = ListNode(curr1.val)
            copy.next = curr1.next 
            curr1.next = copy
            curr1 = copy.next
        
        curr2 = head
        while curr2 and curr2.next:
            original = curr2
            copy = curr2.next
            if original.random:
                copy.random = original.random.next
            else:
                copy.random = None
            curr2 = curr2.next.next

        curr3 = head 
        original_head = head
        copy_head = head.next
        while curr3 and curr3.next:
            original = curr3
            copy = curr3.next
            curr3 = curr3.next.next
            
            original.next = original.next.next 
            if copy.next:
                copy.next = copy.next.next
            else:
                copy.next = None 
            
            
        return copy_head 
            
