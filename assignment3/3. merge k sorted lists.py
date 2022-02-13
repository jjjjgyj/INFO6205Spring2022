class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        test = [1,2,3]
        
        return self.split(lists, 0, len(lists) - 1)
    
    def split(self, lists, start, end):
        if end - start == 0:
            return lists[start]
        
        mid = (start + end) // 2
        l = self.split(lists, start, mid)
        r = self.split(lists, mid + 1, end)
        return self.merge(lists, l, r)
        
    def merge(self, lists, left, right):
        curr = dummy = ListNode(None)
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        
        return dummy.next 
        
        
        
        
        
        
        
        
        
        
