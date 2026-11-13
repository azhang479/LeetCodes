# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Halfway through the linked list, it swap
        #We could maintain a list, O(n) that tracks all the nodes. Once we get to the end, we iterate through and assign them with 2 pointers. That's O(n) space and O(n) time. 

        curr = head
        nodeList = []
        while curr:
            nodeList.append(curr)
            curr = curr.next
        
        l = 0
        r = len(nodeList) - 1
        #If even, this will end on l == r where we can assign it's next to None
        #If l != r, then l > r, which means we need to assign l's to None since they crossed and it is incorrectly assigned at the moment
        #Actually that means we can always assign l's next to None since the conditions cross
        while l < r:
            nodeList[l].next = nodeList[r]
            nodeList[r].next = nodeList[l + 1]
            l += 1
            r -= 1
        

        nodeList[l].next = None
        