class Solution:
    def longestPalindrome(self, s: str) -> str:
        #2D dp array,
        #each cell [i][j] holds True if i --> j is a palindrome and False if not
        #only half the arary need to be used since i < j doesnt make sense
        #Base cases are cells[i][i] = True
        #A palindrome is a palindrome if first and last letters are the same and if the interior letters are the same.
        #So, if cells[i+1][j-1] is a palindrome and s[i] == s[j], then it is a palindrome.

        #We are also going to do an O(n^2) time and O(1) space using expand around center
        #Basically, for each letter, expand left and right until letters dont match, keeping track of the max values.

        max_length = 1
        max_l = 0
        max_r = 0
        #for each letter:
        for center in range(len(s)):
            #Odd centers
            l = center
            r = center
            #Check left and right 
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if max_length < r - l + 1:
                        max_length = r - l + 1
                        max_l = l
                        max_r = r
                else:
                    break
                l -= 1
                r += 1
            #even centers
            l = center
            r = center + 1
            #check left and right
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if max_length < r - l + 1:
                        max_length = r - l + 1
                        max_l = l
                        max_r = r
                else:
                    break
                l -= 1
                r += 1
            
        return s[max_l:max_r+1]
