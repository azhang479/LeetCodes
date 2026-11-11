class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        #Sort s and g, O(xlogx) operations
        s.sort()
        g.sort()
        #Then, go through all s and match with smallest possible g. This is okay since we want to maximize the number of cookies used and they are sorted. So, if a smaller g uses a cookie that could've gone to a bigger g, that bigger g will either not find a cookie (would've had the same cookie smaller g took so thats the same) or find a cookie (smaller g used a smaller cookie that bigger g may not have been able to use instead of the one it was able to use)
        cookie = 0
        totalCookies = len(s) 
        numSatisfied = 0
        for child in g:
            #Cookie is smaller than the current smallest child, no other child can have it, so we move on
            while cookie < totalCookies and s[cookie] < child:
                cookie += 1
            
            #If we run out of cookies, we can stop
            if cookie >= totalCookies:
                return numSatisfied

            #Child takes cookie, another one satisfied
            cookie += 1
            numSatisfied += 1

        return numSatisfied
