# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        #Doing a BFS should allow us to get each level of nodes since each "breadth" would represent a depth.
        if not root:
            return []
        
        queue = deque([root])

        depths = []
        while queue:
            #Each depth will be the ones currently contained in queue
            depth = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                depth.append(curr.val)
            depths.append(depth)

        return depths