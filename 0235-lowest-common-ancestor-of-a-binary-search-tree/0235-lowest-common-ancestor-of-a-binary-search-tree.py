# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #The lowest node must be where p and q split. Since its a binary search tree, one must be on the left and one on the right. So, we just find the value where 
        #search downwards since we cant go up and we must search
        #At each node, 
        #If both numbers (l and r) are between p and q, then that is the split since one must be on the left subtree and one on the right subtree
        #If only 1 number or 1 number between them, we search down that number. 
        #If we reach a number, exactly before returning,

        #let me try if 1 number is to the left and 1 to the right of root, then we return?
        #and then if we reach a number we return it

        curr = root

        while True:
            if curr.val == p.val or curr.val == q.val:
                return curr
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
            