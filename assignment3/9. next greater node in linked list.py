class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]
        
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
   
        result = [0] * len(node_list)
        stack = []
        for i in range(len(node_list)):
            while stack and node_list[i] > stack[-1][1]:
                result[stack[-1][0]] = node_list[i]
                stack.pop()            
            else:
                stack.append((i, node_list[i]))
        
        return result
        
            
