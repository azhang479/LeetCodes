class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #Non DP version can just use past 2 values:
        #L represents left stair, R represent right stair
        #Each one stores cost including the cost to step on that stair
        minCostL = cost[0]
        minCostR = cost[1]
        for i in range(2, len(cost)):
            newMinCost = min(minCostL, minCostR) + cost[i]
            minCostL = minCostR
            minCostR = newMinCost
        
        return min(minCostL, minCostR) #includes stair values so the min is going to be minimum of both as both can take you up to the top.

 
        #dp solution: have an array of 1xn, each one representing the min cost to reach this stair
        #min found by min of last 2 plus their costs
        #base case is stair 1 with cost of cost[1] and stair 2 with cost[1]

        minCost = [0] * len(cost)
        minCost[0] = 0 #can start here with cost[0] to step on next step
        minCost[1] = 0 #can start here with cost[1] to step on next step
        for i in range(2, len(cost)):
            minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])
        
        #one last step to reach the top
        last = min(minCost[-1] + cost[-1], minCost[-2] + cost[-2])

