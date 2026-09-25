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
        # create new node for curr node
        # for each neighbor of curr node
        # if neighbor has NOT been created yet -> recursively call func to create new node
        # else -> get the existing clone of neighbor
        # return curr node

        def clone(node, copies):
            if node is None:
                return
            
            copy = Node(node.val)
            copies[copy.val] = copy

            for n in node.neighbors:
                if n.val in copies:
                    copy.neighbors.append(copies[n.val])
                else:
                    copy.neighbors.append(clone(n, copies))

            return copy

        return clone(node, {})