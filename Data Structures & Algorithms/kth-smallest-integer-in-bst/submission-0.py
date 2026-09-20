# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            return 0
        
        i = 0
        ans = None
        
        def findK(node):
            nonlocal i
            nonlocal ans

            if node is None or ans:
                return

            findK(node.left)
            i += 1
            if i == k:
                ans = node.val
                return
            findK(node.right)

        findK(root)

        return ans