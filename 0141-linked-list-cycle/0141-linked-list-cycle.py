# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #one way would be to have a set that contains all the visited positions, O(n) storage space and O(n) time
        #We could also brute force where on each node we traverse until either end of list or reach back to current node, O(n^2)
        #We want something less than O(n) storage space and less than O(n^2) time

        #If no linked list or 1 element, no cycle
        if not head or not head.next:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False

        
        
        