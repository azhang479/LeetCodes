# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        #The smallest value is the leftmost value
        #We want a recursive function since it might be on the right side of a left node?
        #So keep a priority queue that goes until either we reach the leftmost value or if it is full?
        #Basically, if we reach the left most value (no more none.left), we recurse back up the stack and check .right and all the way down its left tree. If priority queue isnt full yet, we do that again.
        
        #Actually, we can recurse all the way down left and start counting up which is a more space efficient implementation
        self.counter = 0
        self.val = -1 
        self.DFS(root, k)
        return self.val

    def DFS(self, root, k):
        if not root:
            return
        if self.counter > k:
            return 
        
        self.DFS(root.left, k)

        self.counter += 1
        if self.counter == k:
            self.val = root.val
                
        self.DFS(root.right, k)
        return