class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num2Dict = {} #Stores {num: next_greatest}
        end = len(nums2) - 1
        stack = []
        popped = 0

        #O(m) operation since we loop once, each one does O(1) work (can do up to m on 1 element but each element only gets added/removed once O(1) so O(1) max)
        for i in range(len(nums2)):
            element = nums2[end - i]
            #Remove stack values until element is less than top of stack (next greater found) or stack empty (no greater)
            while stack and element > stack[-1]:
                stack.pop()

            #If stack is empty, then there is no next greater element
            if not stack:
                num2Dict[element] = -1
            else:
                num2Dict[element] = stack[-1]
            
            stack.append(element)

        ret = []
        #Go through the elements of nums1 and get the next greatest
        for element in nums1:
            ret.append(num2Dict[element])

        return ret
            
            
