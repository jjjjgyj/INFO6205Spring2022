class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        self.result = 0
        cache = {0:1}
        
        self.dfs(root, targetSum, 0, cache)
        
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  

        currPathSum += root.val
        oldPathSum = currPathSum - target

        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1
