class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #DP method:
        #Have an array answer that tracks # of days before a warmer day
        #Work from back to front, tracking temp using a stack. 
        #Basically, if a day n is warmer than day n + 1, all days before day n will use day n as the next warmest day, not day n + 1
        #So, we have a stack([(temp, index)]). Every temperature, we check the stack
        #If the top of the stack is warmer, then we have just a 1, since always add at end of loop. Since we probably want cleaner code, we can do stackInd - currInd anyways as it should be 1.
        #If top of stack is not warmer, we can pop it until empty or there is a warmer one. Any values before us that would've used that value use our value instead. 
        #Then, we always push our (value, curr index). 
        #answer will save [stackInd - currInd]

        stack = []
        length = len(temperatures) - 1
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            indx = length - i
            curr = temperatures[indx]
            
            #Pop from stack until empty or temp is greater than current temp
            while stack and stack[-1][0] <= curr:
                stack.pop()

            if stack:
                #Our answer is the warmer index - current index for difference if stack isnt empty 
                answer[indx] = (stack[-1][1] - indx)
            
            #if stack is empty, we can just skip as it is set to baseline 0
            stack.append((curr, indx))

        return answer