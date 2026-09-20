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
        
        # ans = 0

        def findGood(node, maxVal):
            if node is None:
                return 0
            
            ans = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal, node.val)

            ans += findGood(node.left, maxVal)
            ans += findGood(node.right, maxVal)

            return ans

        return findGood(root, root.val)
        # return ans