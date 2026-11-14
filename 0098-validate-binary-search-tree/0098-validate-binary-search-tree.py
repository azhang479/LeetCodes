# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        #DFS format, each node has a MIN/MAX value to check against, overwritten when possible and transferred when not.
        #Every search left gives a new strict MAX value, every search right gives a strict MIN value

        return self.DFS(root, -float("inf"), float("inf"))

    def DFS(self, root, minVal, maxVal):
        if root == None:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False
        
        return self.DFS(root.left, minVal, root.val) and self.DFS(root.right, root.val, maxVal)
        