class Solution:
    def findMin(self, nums: list[int]) -> int:
        #since log of n times, I'd imagine we try to find the rotation in log(n) then index into that position directly to find min
        #probably something with binary search since log(n)?
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        l = 0
        r = len(nums) - 1
        midpoint = 0
        while l < r:
            midpoint = (r - l) // 2 + l
            #if midpoint < r, right side is sorted up to but not including midpoint
            if nums[midpoint] < nums[r]:
                r = midpoint
            else:
                l = midpoint + 1
        return nums[l]
        #while l <= r:
        #    midpoint = (r - l) // 2 + l
            #minimum has to satisfy this since they are sorted unique numbers
        #    isMin = nums[midpoint] < nums[midpoint - 1]
            #If it is the minimum, we return the number directly
        #    if isMin:
        #        return nums[midpoint]
    
            #If its not minimum, we can compare left, mid, and right
            #if left > midpoint, minimum must be on left side
            #else, minimum must on the right side
        #    elif (nums[l] > nums[midpoint]):
        #        r = midpoint - 1
        #    elif (nums[midpoint] < nums[r]):
        #        r = midpoint - 1
        #    else:
        #        l = midpoint + 1
        