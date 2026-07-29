# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        if root is None:
            return 0

        def calc_diameter(node):
            if node is None:
                return 0
            
            left_length = calc_diameter(node.left)
            right_length = calc_diameter(node.right)

            self.max_diameter = max(self.max_diameter, left_length + right_length)

            # print(node.val, left_length, right_length, '|', left_length + right_length)

            return 1 + max(left_length, right_length)

        calc_diameter(root)

        return self.max_diameter