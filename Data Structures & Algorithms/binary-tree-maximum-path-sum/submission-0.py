# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return sum

        maxSum = -999999

        def findSum(node):
            nonlocal maxSum

            if node is None:
                return 0
            

            leftSum = findSum(node.left)
            rightSum = findSum(node.right)

            currMax = max(node.val, node.val + leftSum, node.val + rightSum) # max of possible paths to add
            maxSum = max(maxSum, currMax, node.val + leftSum + rightSum) # max of overall + possible values at curr node

            print(node.val, leftSum, rightSum, currMax, maxSum)

            return currMax

        findSum(root)
        return maxSum



        