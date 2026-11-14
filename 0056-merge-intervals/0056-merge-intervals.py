class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #We want to start from the earliest interval and keep a "max end time" variable allocated.
        #If the next earliest interval is before max end time, we can keep it in 1 interval. If not, we must start a new interval. 
        if len(intervals) == 1:
            return intervals
        
        retIntervals = []
        intervals.sort()
        currStart = intervals[0][0]
        maxEnd = intervals[0][1]
        for interval in intervals:
            #If the start of the next interval <= the maxEnd, we can merge and set a new max end
            if interval[0] <= maxEnd:
                maxEnd = max(maxEnd, interval[1])
                continue
            
            #If not, then we append the new interval 
            retIntervals.append([currStart, maxEnd])
            currStart = interval[0]
            maxEnd = interval[1]
        #have to append one last one for the last interval 
        retIntervals.append([currStart, maxEnd])

        return retIntervals