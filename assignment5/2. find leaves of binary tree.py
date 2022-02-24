class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:        
        results = []
        self.helper(root, results)
        return results 

    def helper(self, node, results):
        if not node:
            return -1 
        left = self.helper(node.left, results)
        right = self.helper(node.right,results)
        curr_level = max(left, right) + 1 
        self.add_leaf(curr_level, node.val, results)
        node.left, node.right = None, None 
        return curr_level

    def add_leaf(self, curr_level, value, results):
        if curr_level == len(results):
            results.append([])
        results[curr_level].append(value)
        
