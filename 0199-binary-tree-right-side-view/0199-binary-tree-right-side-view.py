# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        #This is just the right mode value of BFS I think?
        #Since BFS is depth based traversal, and this algorithm is asking us to look from the right and find the element we'd see, should be the rightmost element of each depth.
        queue = deque([root])
        rightSide = []
        if not root:
            return []
        while queue:
            curr = None
            #depth based BFS, 
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #Curr should be the last element on each depth, 
            rightSide.append(curr.val)

        return rightSide
        

            