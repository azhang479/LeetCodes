# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        #DFS down the tree, comparing right and left depths gong back upwards
        if not root:
            return True
        if self.DFS(root) == -1:
            return False
        return True
        

    def DFS(self, root):
        if root is None:
            return 0
        
        l_depth = self.DFS(root.left)
        r_depth = self.DFS(root.right)
        if l_depth == -1 or r_depth == -1:
            return -1

        depth_diff = l_depth - r_depth

        #Unbalanced, return False
        if depth_diff < -1 or depth_diff > 1:
            return -1
        
        #return our depth
        return max(l_depth, r_depth) + 1
