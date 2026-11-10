class Solution:
    def rob(self, nums: list[int]) -> int:
        #given an array [1, 2, 3, 4, 5, etc.]
        #pick out all the values to maximize total
        #avoid picking out 2 simultaneous values
        #The maximum amount of money at each house is equal to robbing max(houses[i-2], houses[i-3], etc.)
        #Basically, since only the singular previous house matters, we can check the max of all the previous houses each run and set our value = max(previous) + our value
        #Actually, only the previous 3 houses matter. We skip one house and teh previous 2 houses will be the max of the rest of them + their house value, so we dont need to check the rest
        #val[i] = max(val[i - 2], val[i - 3]) + houses[i]

        #If nums is len 1, return the single value for max
        #If nums is len 2, the max is the max of those 2
        #If nums is len 3, the max is either nums 0 + 2 or nums 1
        #This set up is not required but makes the loop cleaner
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        val = [0] * len(nums)
        val[0] = nums[0]
        val[1] = nums[1]
        val[2] = nums[2] + nums[0]
        
        for i in range(3, len(nums)):
            val[i] = max(val[i-2], val[i-3]) + nums[i]

        return max(val[-1], val[-2])