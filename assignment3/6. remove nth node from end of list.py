class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        list_len = 0
        while cur is not None:
            cur = cur.next
            list_len += 1
        if list_len - n <= 0:
            return head.next
        else:
            prev = head    
            for i in range (list_len - n - 1):
                prev = prev.next 
            prev.next = prev.next.next 
            return head
