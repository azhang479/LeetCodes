# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        #I think we use a method where we have a back node and a front node. If a value == 9, the back node is there in case we have an overflow on the next digit. This stays the same until we reach a digit that is < 9, then we can move back node since that will hold the overflow digit. If an overflow digit goes on a row of 9's it must traverse the full row. Then, each digit can just be added 
        #Actually, we dont even need to do that since its reverse order. We can just add them and have an overflow bit.
        #we can also modify l1 in place to keep it O(1) space and O(n) time. Modifying the longer one would save some space but it shouldn't be too big of an issue since max 100 nodes
        #Actually we can just modify both in place then at the end work on the longer one
        carryIn = False
        currL1 = l1
        currL2 = l2
        while currL1.next and currL2.next:
            currL1.val += currL2.val
            if carryIn:
                currL1.val += 1
                carryIn = False

            if currL1.val >= 10:
                currL1.val -= 10
                carryIn = True
            currL2.val = currL1.val
            currL1 = currL1.next
            currL2 = currL2.next

        #Do the last addition, cant end on None for the while loop in case l1 is None and we need to add another digit
        currL1.val += currL2.val
        if carryIn:
            currL1.val += 1
            carryIn = False

        if currL1.val >= 10:
            currL1.val -= 10
            carryIn = True
        currL2.val = currL1.val

        #If both lists are empty, we can end here after checking for a possible new node to add
        if not currL1.next and not currL2.next:
            if carryIn:
                currL1.next = ListNode(1)

            return l1

        retL1 = True
        #if l1 is empty
        if not currL1.next:
            head = currL2.next
            retL1 = False
        else:
            head = currL1.next
        
        #Finish off the carry in's necessary in case, end when head.next is none
        while head.next:
            if carryIn:
                head.val += 1
                carryIn = False
            else:
                break
            if head.val >= 10:
                head.val -= 10
                carryIn = True
            head = head.next

        #Do the last addition if needed
        if carryIn:
            head.val += 1
            carryIn = False
        if head.val >= 10:
            head.val -= 10
            carryIn = True
        
        #Might need to add a new node if the last digit created a carry out
        if carryIn:
            head.next = ListNode(1)
            carryIn = False

        if retL1:
            return l1
        else:
            return l2