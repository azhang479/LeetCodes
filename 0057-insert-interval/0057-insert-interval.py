class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #We could do what did before with the max intervals, just add this into the list
        #We can do this by just running the merge intervals, checking the new interval each time to see if it fits there

        if not intervals:
            return [newInterval]
        
        #If we begin with a newInterval:
        if newInterval[0] < intervals[0][0]:
            maxEnd = newInterval[1]
            currStart =newInterval[0]
        else:
            maxEnd = intervals[0][1]
            currStart = intervals[0][0]
        newIntervals = []
        newAdded = False
        for interval in intervals:
            #New interval belongs here in the interval list, check it separately
            if not newAdded and interval[0] > newInterval[0]:
                if newInterval[0] <= maxEnd:
                    maxEnd = max(maxEnd, newInterval[1])
                else:
                    newIntervals.append([currStart, maxEnd])
                    maxEnd = newInterval[1]
                    currStart = newInterval[0]

            if interval[0] <= maxEnd:
                maxEnd = max(maxEnd, interval[1])
                continue
            newIntervals.append([currStart, maxEnd])
            maxEnd = interval[1]
            currStart = interval[0]
        
        #Final check for the new interval if it is at the end
        if not newAdded:
            if newInterval[0] <= maxEnd:
                maxEnd = max(maxEnd, newInterval[1])
            else:
                newIntervals.append([currStart, maxEnd])
                maxEnd = newInterval[1]
                currStart = newInterval[0]

        newIntervals.append([currStart, maxEnd])

        print(f"currStart: {currStart}, maxEnd: {maxEnd}, intervals: {intervals}")

        return newIntervals

