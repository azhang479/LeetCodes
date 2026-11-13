class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #I want to attempt something like a binary search
        #So we know if midpoint < right, then everything to the right is strictly increasing
        #So, we can search only right if midpoint < target < right. Else, the target is on the left
        #If midpoint > right, then we know that midpoint may increase before hitting the first element of the orignal array. In this case, if midpoint < target or right > target we can search right. Else, we can search left side.
        #Since we check midpoint on each run, we can discard midpoint. Since values are distinct, we should eventually reach our target
        l = 0 
        r =  len(nums) - 1
        while l <= r:
            midpoint = (r - l) // 2 + l
            if nums[midpoint] == target:
                return midpoint
            
            #If increasing on right
            if nums[midpoint] < nums[r]:
                #Search right condition
                if nums[midpoint] < target and target <= nums[r]:
                    l = midpoint + 1
                #target is on the left
                else:
                    r = midpoint - 1
            #hit previous start before right
            else:
                #Search right condition
                if (nums[midpoint] < target) or (nums[r] >= target):
                    l = midpoint + 1
                else:
                    r = midpoint - 1
            
        return -1


