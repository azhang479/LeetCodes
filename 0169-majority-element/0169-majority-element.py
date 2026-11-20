class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #Since the majority element is guarenteed to appear more than n/2 times,
        #We can just track a singular "majority element" throughout the whole thing
        curr = nums[0]
        count = 0
        for i in nums:
            if curr == i:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr = i
                count = 1
        return curr

        
        #Not O(1) space
        numNums = {}
        n = len(nums)
        for num in nums:
            numNums[num] = numNums.get(num, 0) + 1
            if numNums[num] > n//2:
                return num
        
        return 

        