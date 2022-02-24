class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        width = 0 
        queue = deque([(root, 0)])
        while queue:
            _, first_col = queue[0]
            for i in range(len(queue)):
                node, col = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * col))
                if node.right:
                    queue.append((node.right, 2 * col + 1))
            
            width = max(width, col - first_col + 1)
            
        return width
                    
