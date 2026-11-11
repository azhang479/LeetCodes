class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        trainer = 0
        maxSatisfied = 0
        for player in players:
            while trainer < len(trainers) and trainers[trainer] < player:
                trainer += 1
            
            if trainer >= len(trainers):
                return maxSatisfied
            
            trainer += 1
            maxSatisfied += 1

        return maxSatisfied
