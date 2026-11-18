class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #distinct integer candidates
        #target integer target
        #unique combos of candidates where numbers sum to target
        #same number can be chosed from candidates unlimited time
        #2 combos are unique if frequency is different (1, 1, 1, 2) and (2, 2, 1) for 5
        
        #For each number
        #if divisible into target, add that combo

        #Then for each number
        #remove 1 of that number from target, check divisibility of all other unchecked numbers and that combo
        #If we find a suitable combo, we can store it in a set and then add that combo to a check list. 
        #Then remove another 1 from target, check again
        #repeat until target <= 0. No need to check this number again since all combos are used
        #O(n^2 solution)
        
        self.stored = []
        
        #For all starting candidates
        self.recurse(0, candidates, [], target)
        
        return self.stored


    def recurse(self, i, candidates, currSet, target):
        #If we reach the target, we found a valid combo
        if target == 0:
            self.stored.append(currSet)
            return
        #If we are below 0, there is no valid combo here since we overshot
        if target < 0:
            return 
        #Else, we can recurse down the chain
        self.recurse(i, candidates, currSet + [candidates[i]], target - candidates[i])
        
        #Also check all the other candidates above the current one
        if i < len(candidates) - 1:
            self.recurse(i+1, candidates, currSet, target)

