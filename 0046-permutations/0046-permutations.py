class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.list = []
        for i in range(len(nums)):
            self.recurse([nums[i]], nums[0:i] + nums[i+1:])

        return self.list

    def recurse(self, curr, nums):
        if len(nums) == 0:
            self.list.append(curr)
            return
        
        for i in range(len(nums)):
            self.recurse(curr + [nums[i]], nums[0:i] + nums[i+1:])
