class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #Basically 2d binary search
        #Since end of last row is less than beginning of next row, we can binary search for the value that our target would be between
        #We can then search the target column.

        l = 0
        r = len(matrix) - 1
        row = 0
        while l <= r:
            if matrix[l][0] == target or matrix[r][0] == target:
                return True
            #since matrix[l][0] < target < matrix[r][0] can be true in multiple circumstances, we can search until matrix[l][0] < target and matrix[r][0] < target and r - l == 1
            midpoint = (r - l) // 2 + l

            print(f"midpoint: {midpoint}, r: {r}, l: {l}")
            if matrix[midpoint][0] == target:
                return True
            
            #If midpoint is < target and midpoint + 1 is < target, we know the target must be in this row. else, we can move the midpoint up like normal since it must be in a greater row
            if matrix[midpoint][0] < target:
                if midpoint + 1 > len(matrix) - 1:
                    row = midpoint
                    break
                if matrix[midpoint + 1][0] > target:
                    row = midpoint
                    break
                l = midpoint + 1
            #if midpoint > target, we know target must be in a previous row (midpoint - 1)
            else:
                r = midpoint - 1
        
        print(row)
        #Then, we just binary search the row 
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            midpoint = (r - l) // 2 + l
            if target == matrix[row][midpoint]:
                return True
            
            if matrix[row][midpoint] < target:
                l = midpoint + 1
            else:
                r = midpoint - 1

        return False