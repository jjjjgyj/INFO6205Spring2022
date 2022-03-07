class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if not left and not right and node.val == target:
                return None
            return TreeNode(node.val, left, right)

        return dfs(root)
