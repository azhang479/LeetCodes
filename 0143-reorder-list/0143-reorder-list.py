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
        #we want to basically find the middle of the list, reverse the second half, and then alternate left right assignments moving in on each one. 
        #The last one must be assigned to None
        #This can be done in O(n) time and O(1) space by using slow/fast pointers
        #We can do when fast.next exists, fast will be assigned to None on the last,
        #The one that slow is on will always be the last one, so we can assign that None.
        #Then, we move in from left and right, starting from the left. 
        #We assign left.next = right, then move left in 1. Then, right.next = left, move right in one. Continue until one of the pointers == slow.
        #Reversing the second half of the list can be done in place as well using a pointers approach.

        #Find the middle
        slow = head
        fast = head
        #If 1 node, just return head
        if not head.next:
            return head

        #Only 2 nodes, flip them and return
        if not head.next.next:
            return head
            
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #Now, starting from slow, flip the next pointers, effectively splitting it into 2 lists pointing inwards
        curr = slow.next
        prev = slow
        while curr and curr.next:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        curr.next = prev
        #curr is now the right head, head is still the left head. 
        slow.next = None
        l = head
        r = curr

        while l != slow and r != slow:
            temp = l
            l = l.next
            temp.next = r
            temp = r
            r = r.next
            temp.next = l
        
        
