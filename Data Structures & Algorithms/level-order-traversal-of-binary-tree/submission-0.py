# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        
        res = defaultdict(list)

        def findLevelOrder(node, level):
            if node is None:
                return
            
            res[level].append(node.val)
            findLevelOrder(node.left, level + 1)
            findLevelOrder(node.right, level + 1)
        
        findLevelOrder(root, 0)
        
        return list(res.values())