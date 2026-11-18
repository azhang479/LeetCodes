"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Given connected undirected graph
        #Clone the graph and return it
        #start from node
        #copy adjacency matrix
        #Go to the rest of the nodes
        #copy adjacency matrix


        #We have a dict that maps {old node -> new node}
        #Then, we BFS. Queue stores old nodes. 
        #If that old node is in the dict, we retrieve it and update neighbors. 
        #The neighbors are based on old node and if the neighbor has a mapping we retrieve that and link. If not, we create a new node/mapping.
        #
        if not node:
            return 
        queue = deque([node])
        mapping = {}
        newNode = Node(node.val, [])
        mapping[node] = newNode

        while queue:
            curr = queue.pop()
            #This should always exist since we create new one on enqueue 
            currNode = mapping[curr]

            #If the neighbor is mapped, we assume it is in the queue and just link
            #If neighbor is not mapped, create new one, map, add to queue, and link
            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    new = Node(neighbor.val, [])
                    mapping[neighbor] = new
                    queue.append(neighbor)
                currNode.neighbors.append(mapping[neighbor])

        return newNode

