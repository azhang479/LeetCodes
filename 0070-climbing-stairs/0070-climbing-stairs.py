class Solution:
    def climbStairs(self, n: int) -> int:
        #Track how many ways there are to get to n - 1 and n - 2
        #Use that to track how many ways to get to n
        #distinct ways is just distinct ways to get to n - 1 + n - 2 + 2

        #For n = 4,
        #1, 1, 1, 1
        #2, 1, 1,
        #1, 2, 1
        #1, 1, 2
        #2, 2, 

        #For n = 5,
        #1, 1, 1, 1, 1
        #1, 1, 1, 2,
        #1, 1, 2, 1,
        #1, 2, 1, 1,
        #2, 1, 1, 1,
        #1, 2, 2,
        #2, 1, 2,
        #2, 2, 1,

        if n == 1:
            return 1
        ways = [0] * (n + 1)
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2
        #For each next way
        for i in range(2, n):
            ways[i + 1] = ways[i] + ways[i - 1]#unique ways to get to n - 1 + unique ways to get to n - 2, then 1 step and 2 step, 
        return ways[-1]