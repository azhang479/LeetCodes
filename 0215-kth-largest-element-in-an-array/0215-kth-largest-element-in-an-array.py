class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #Basically, we want a data structure that allows us to store up to k elements so we can know what the kth largest is
        #To effectively do this, we can use a minheap as it will have the smallest element on the head.
        #If we store k elements, the smallest of the k elements will be the kth largest.
        heap = []

        for num in nums:
            if len(heap) >= k:
                if (num > heap[0]):
                    heapq.heapreplace(heap, num)
            else:
                heapq.heappush(heap, num)
        return heap[0]