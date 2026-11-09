class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Each time we encounter a 1, BFS from it and have a visited set of coordinates
        visited = set()
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #If the element is a 1 and not already visited, we generate a new queue with it
                if grid[i][j] == "1" and (i, j) not in visited:
                    q = deque([(i, j)])
                    #For every element in the queue
                    while q:
                        #Append current element to visited
                        m, n = q.popleft()
                        visited.add((m, n))
                        #For all possible directions
                        for dr, dc in directions:
                            nextRow = m + dr
                            nextCol = n + dc
                            #If it is a valid direction, it is a 1 on the grid, and it hasn't been visited
                            if ((nextRow != -1) and (nextCol != -1) and (nextRow < len(grid)) and (nextCol < len(grid[0])) and (grid[nextRow][nextCol] == "1") and ((nextRow, nextCol) not in visited)):
                                #append that to the deque for BFS
                                q.append((nextRow, nextCol))
                                #Mark as visited
                                visited.add((nextRow, nextCol))
                    islands += 1 #increment the islands by 1, all connecting land counted for

        return islands


                        

                    
