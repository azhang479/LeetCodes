class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        #max depth BFS?
        #Search full grid, count all rotting orange islands using BFS, saving maximum depth. 
        #cant just be regular BFS since if we run into more rot on the other side it coulda reached our orange faster
        #We could start at every index with rotting but then we lose some efficiency. Max depth also wouldnt work because its minimum minutes

        #Update full grid each turn, but check/update frontier nodes only
        #Use a set of frontier nodes to save some space
        #Basically BFS but with multiple roots at once
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        depth = 3
        #starting with all the rotten oranges, 
        while queue:
            #Update all the current frontier ones
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in directions:
                    curr_i = x + i
                    curr_j = y + j
                    if curr_i < 0 or curr_j < 0 or curr_i >= len(grid) or curr_j >= len(grid[0]):
                        continue
                    if grid[curr_i][curr_j] == 1:
                        grid[curr_i][curr_j] = depth
                        queue.append((curr_i, curr_j))
                
            depth += 1
        
        max_depth = 2
        #once queue is empty, all squares that have been rotted have rotted. If a 1 exists, then return -1. Else, return the max depth.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                max_depth = max(grid[i][j], max_depth)

        return max_depth - 2
