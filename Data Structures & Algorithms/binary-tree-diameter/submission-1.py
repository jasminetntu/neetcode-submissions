# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_diameter = 0
        def calc_diameter(node):
            nonlocal max_diameter

            if node is None:
                return 0
            
            left_length = calc_diameter(node.left)
            right_length = calc_diameter(node.right)

            max_diameter = max(max_diameter, left_length + right_length)

            # print(node.val, left_length, right_length, '|', left_length + right_length)

            return 1 + max(left_length, right_length)

        calc_diameter(root)

        return max_diameter