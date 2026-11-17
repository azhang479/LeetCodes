class Solution:
    def rob(self, nums: list[int]) -> int:
        #Break the last house (no more circle)
        #Have 2 lists, max value for must choose house, max value for must not choose house
        #If choose first house, last house means you cant choose the first house
        #If not choose first house, we can freely choose the last one

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1],nums[0])
        #For not choosing the first house, max value starts at max(house1, house2)
        #Then, recursion is maxN = max(house-2 + house, house-1) starting at house 3
        maxNL = nums[1]
        maxNR = max(nums[1], nums[2])
        #max NR is the right max, NL is the left max (houses -1 and -2)
        for i in range(3, len(nums)):
            temp = maxNR
            maxNR = max(maxNR, maxNL + nums[i])
            maxNL = temp

        maxCL = nums[0]
        maxCR = max(nums[0], nums[1])
        #max NR is the right max, NL is the left max (houses -1 and -2)
        for i in range(2, len(nums)):
            temp = maxCR
            maxCR = max(maxCR, maxCL + nums[i])
            maxCL = temp
        
        #maxCL is max of choosing house 1, not choosing last house yet
        #maxCR is the max of choosing last house and house 1, 
        #maxNR is the max of not choosing house 1, possibly choosing last house
        #maxNR should be equal to max CR - house 1

        #total max would be max(maxCL, maxNR)
        return max(maxCL, maxNR)



        