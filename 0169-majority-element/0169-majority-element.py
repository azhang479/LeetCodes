class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numNums = {}
        n = len(nums)
        for num in nums:
            numNums[num] = numNums.get(num, 0) + 1
            if numNums[num] > n//2:
                return num
        
        return 

        