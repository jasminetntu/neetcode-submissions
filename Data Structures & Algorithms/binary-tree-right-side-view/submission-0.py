# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.findRight(root, [], 0)

    def findRight(self, node, res, level):
        if node is None:
            return res
        
        if level == len(res):
            res.append(node.val)

        self.findRight(node.right, res, level + 1)
        self.findRight(node.left, res, level + 1)

        return res