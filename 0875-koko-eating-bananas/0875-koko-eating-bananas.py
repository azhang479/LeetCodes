class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #max eating speed is max(piles), any faster doesnt make sense as we already reached min time with 1 pile per hour
        #This happens at h = len(piles)
        if h == len(piles):
            return max(piles)
        
        #We need a search algorithm for 1 ... max(piles)
        #Binary search is fastest 
        #O(log(max(piles))) to find the number, O(n) search on the list if we iterate through piles, O(nlog(k)) time 

        #binary search, we want to search for next value = h
        #We should search for which value is >= h but value to the left is < h as this would be minimum of k
        l = 0 #represents maximal k where k is still infeasible (> h total hours)
        r = max(piles) #represents minimal k where k is feasible (<= total hours)
        #Stop at l < r, l is max infeasible, r is min feasible, answer is r
        while l < (r - 1):
            midpoint = (r - l) // 2 + l

            #Hours tracks total hours it would take to eat all bananas
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/midpoint)

            #If hours > h, then we are still infeasible. We want to move l in            #Midpoint could still be a feasible answer for l, so we only move to midpoint
            if hours > h:
                l = midpoint
            else:
                r = midpoint
        #l and r should now be the point where hours(l) > h but hours(l + 1) <= h
        return r