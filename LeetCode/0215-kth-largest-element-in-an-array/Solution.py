import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #brute force solution would be to search k times for largest element which is O(n^2)
        #We could search for k/2 elements since we could search for kth smallest or len - kth largest but still O(n^2)
        #We could sort and pick out the kth element which would be O(nlogn)
        heap = []
        for element in nums:
            if len(heap) >= k:
                if (heap[0] < element):
                    heapq.heappop(heap)
                    heapq.heappush(heap, element)
            else:
                heapq.heappush(heap, element)
        return heap[0]