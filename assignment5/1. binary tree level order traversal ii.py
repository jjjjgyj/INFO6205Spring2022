class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res 
        
        queue = deque([root])
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res[::-1]
