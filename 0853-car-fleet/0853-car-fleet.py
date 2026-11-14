class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        #n cars 
        #each x miles from 0 and traveling to target
        #Given position and speed of car i using position[i] speed[i]
        #Car cannot pass another car but can catch up and travel together at min speed
        #car fleet is single car or gorup fo cars next to each other
        #speed of fleet is minimum speed of all cars in fleet
        #Catching up @ target counts as part of fleet
        #Return # of car fleets

        #O(n^2) by updating each position with the speed and counting until all fleets reach the target


        #We could do sort each position, both the speed and position lists
        #Then, subtract the position from the target to find distance left
        #Divide by speed to find "time units" left
        #Then, we iterate through this time units list. If the value stays the same or goes down, we know that we are capped by the first time unit and it will take that many time units to get to the target
        #This is because they started ahead (list is sorted) so if a car takes 7 time units and a car behind it takes 4 time units, the one with 4 time units will catch up and form a fleet with the 7 time unit one. 
        #it is same or goes down since cars that arrive at target together are same fleet. 
        #If it goes up, we have a new fleet. 
        
        #zip can zip 2 arrays together into tuples
        #Sorted sorts by the first in the tuple
        #zip(*...) unzips into multiple tuples
        #Cast them back into list
        zipped = sorted(zip(position, speed), reverse=True)

        #how many time units left until the target
        totalFleets = 0
        currMax = 0

        for i in range(len(zipped)):
            distance = target - zipped[i][0]
            timeUnits = distance / zipped[i][1]
            
            if (timeUnits > currMax):
                totalFleets += 1
                currMax = timeUnits

        return totalFleets

    #Just submitted and got 
    #position = [8,3,7,4,6,5]
    #speed = [4,4,4,4,4,4]
    #Wrong.

    #I assumed that cars must drive "speed" all at once but this is incorrect.
    #In this example, car 8 will reach before 7, then 6, then 5, then 4, then 3. None simultaneously. 
    #This is because I rounded time units to a ceil. I think if I don't round it it should work?
    #Does work