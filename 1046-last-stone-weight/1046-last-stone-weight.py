class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapify_max(stones) #O(n), creates a max heap
        print(stones)
        while len(stones) >= 2:
            y = heapq.heappop_max(stones) #heaviest stone
            x = heapq.heappop_max(stones) #second heaviest stone
            if y != x:
                heapq.heappush_max(stones, y - x)
        
        if stones:
            return stones[0]
        return 0
