class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        #Keep a visited set? once you visit a new value, we can create all the combos with the previously visited?
        
        powerSet = [[]]
        for i in range(len(nums)):
            for arr in powerSet.copy():
                powerSet.append(arr + [nums[i]])

        return powerSet

