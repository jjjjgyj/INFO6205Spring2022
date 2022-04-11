"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # find all nodes and put into set
        visited = self.findNode(node)
        
        # copy all nodes and put into a map
        mapping = self.copyNode(visited)
        
        # copy all edges
        mapping = self.copyEdge(mapping)
        
        return mapping[node]
    
    def findNode(self, node):
        visited = set()
        queue = deque()
        queue.append(node)
        visited.add(node)
        
        while queue:
            curr_node = queue.popleft()
            for nei in curr_node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return visited
    
    def copyNode(self, visited):
        mapping = {}
        for each_node in visited:
            mapping[each_node] = Node(each_node.val)
        return mapping
    
    def copyEdge(self, mapping):
        for each_node, copy_node in mapping.items():
            for nei in each_node.neighbors:
                copy_node.neighbors.append(mapping[nei])
        return mapping
        
