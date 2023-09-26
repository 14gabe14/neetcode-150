"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        copied_nodes = {node.val: Node(node.val)}
        nodes_to_explore = deque([node])

        while nodes_to_explore:
            original = nodes_to_explore.popleft()
            copy = copied_nodes[original.val]

            for neighbor in original.neighbors:
                if neighbor.val not in copied_nodes:
                    copied_nodes[neighbor.val] = Node(neighbor.val)
                    nodes_to_explore.append(neighbor)
                
                copy.neighbors.append(copied_nodes[neighbor.val])

        return copied_nodes[node.val]