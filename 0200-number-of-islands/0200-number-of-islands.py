class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #We could use a BFS method where we search through all the grid slots and each time we have a "1", we mark all adjacent spots in a visited set to create the island. Then, each new "1" will be a new island that runs the BFS again. 
        #O(mn) solution since we work through all the slots once in O(1) time
        #However, this is O(mn) space as well

        #We can do it in place by modifying the array itself, for example setting all the visited "1"'s to "2"'s to mark visited. This would be O(mn) time and O(1) space
        adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #If we reach a 1, we run BFS and "add an island"
                if grid[i][j] == "1":
                    queue = [(i, j)]
                    grid[i][j] = "2"
                    total_islands += 1
                    while queue:
                        curr_i, curr_j = queue.pop()
                        for x, y in adjacent:
                            #Check all adjacent ones
                            check_x = curr_i + x
                            check_y = curr_j + y
                            #out of range
                            if (check_x == -1 or check_x >= len(grid) or check_y == -1 or check_y >= len(grid[0])):
                                continue
                            
                            #If it is a 1, add to visited by setting to 2 and add to queue
                            if grid[check_x][check_y] == "1":
                                grid[check_x][check_y] = "2"
                                queue.append((check_x, check_y))

        return total_islands

                        