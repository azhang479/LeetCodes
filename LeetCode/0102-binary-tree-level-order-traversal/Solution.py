# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        #basically BFS?
        if not root:
            return []
        queue = deque([(root, 0)])
        ret = [[]]
        currDepth = 0
        while queue:
            currNode, depth = queue.popleft()
            if depth != currDepth:
                currDepth = depth
                ret.append([])
            ret[currDepth].append(currNode.val)
            if currNode.left: queue.append((currNode.left, depth + 1))
            if currNode.right: queue.append((currNode.right, depth + 1))
        return ret