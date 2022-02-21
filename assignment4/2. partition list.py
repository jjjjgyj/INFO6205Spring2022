class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = head
        while j:
            if j.val < x:
                if j == i.next:
                    i = j
                    prev = j
                    j = j.next
                else:
                    tmp1 = i.next
                    i.next = j
                    tmp2 = j.next
                    j.next = tmp1
                    prev.next = tmp2
                    i = j
                    j = tmp2
            else:
                prev = j
                j = j.next
        return dummy.next
