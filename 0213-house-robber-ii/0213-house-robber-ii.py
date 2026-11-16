class Solution:
    def rob(self, nums: list[int]) -> int:
        #Create a DP array, [nx1] where each cell i is max money you can steal at that house
        #This is either the value of 2 houses before it + itself or the max of the house value before it, which assumes we dont steal our house. Whatever is max 

        #We can disconnect the last house, and do hosue robber on the rest of the houses
        #We could have a [nx2] matrix to also mark which houses were chosen

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        #houses is strictly including first house
        #housesN is strictly not including first house
        houses = [0] * len(nums)
        housesN = [0] * len(nums)
        houses[0] = nums[0]
        housesN[0] = 0
        houses[1] = nums[0]
        housesN[1] = nums[1]

        #save last house to break the loop
        #Keep a count if the first house has been robbed
        for i in range(2, len(nums)):
            houses[i] = max(houses[i-1], houses[i-2] + nums[i])
            housesN[i] = max(housesN[i-1], housesN[i-2] + nums[i])

        #max value is houses[-2] or houses[-3] (strictly including first house means not including last house), or housesN[-1] or housesN[-2]

        return max(houses[-2], houses[-3], housesN[-1], housesN[-2])

        