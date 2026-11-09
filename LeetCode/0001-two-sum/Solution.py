class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, val in enumerate(nums):
            mydict[val] = i

        for i in range (0, len(nums)):
            diff = target - nums[i]
            if (diff in mydict) and (mydict[diff] != i):
                return [min(mydict[diff], i), max(mydict[diff], i)]
