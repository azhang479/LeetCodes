# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.recurse(root)
        return self.max

    def recurse(self, root):
        if root is None:
            return 0
        leftVal = self.recurse(root.left)
        rightVal = self.recurse(root.right)

        self.max = max(leftVal + rightVal, self.max)

        return max(leftVal, rightVal) + 1
