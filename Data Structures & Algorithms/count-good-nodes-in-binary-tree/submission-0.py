# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # keep track of max so far
        # go left 
        # if node.val < max -> not good, else if >= max then good (+1 ans)
        # go right
        # update max if theres new max

        if root is None:
            return 0
        
        ans = 0

        def findGood(node, maxVal):
            nonlocal ans

            if node is None:
                return
            
            if node.val >= maxVal:
                ans += 1

            newMax = max(maxVal, node.val)

            findGood(node.left, newMax)
            findGood(node.right, newMax)

        findGood(root, root.val)
        return ans