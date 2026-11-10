class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #We want a data structure that can efficiently store largest x elements
        #We can use a manually managed set/list
        #Min heap works
        #We can have a minheap that tracks largest k elements, with removal of the head (min) when we have more than k elements

        heap = []

        for num in nums:
            #If heap is full
            if len(heap) >= k:
                #If the smallest element in the heap is less than our current number
                if num > heap[0]:
                    heapq.heappop(heap) #Remove smallest element
                    heapq.heappush(heap, num) #push new element
            else:
                #If heap isnt full, we can just insert
                heapq.heappush(heap, num)

        #Heap will always contain the largest k elements now with the minimum being the kth largest
        return heap[0]