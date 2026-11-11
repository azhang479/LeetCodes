class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #O(n^2) solution: check every subarray
        #We could do this with DP.
        #[nx1] array, each cell represents "max value" of subarrays up to that point
        #so maximal[n] should be = max(0, maximal[n-1]) + nums[n]
        #This is because if a previously seen subarray, [n-1], is maximally negative, it will not start our new subarray.
        #Since its a subarray, n must be added, so + nums[n] works
        #Cant just store 1 max value since we may go down a lot before coming back up and theres no way to really know I dont think?
        if len(nums) == 1:
            return nums[0]

        #Set up first element of array 
        maximal = [nums[0]]

        #For each element after the first, append a new max sum
        for i in range(1, len(nums)):
            maximal.append(max(maximal[i - 1], 0) + nums[i])
        
        return max(maximal)