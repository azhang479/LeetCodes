class Solution:
    def longestPalindrome(self, s: str) -> str:
        #2D dp array,
        #each cell [i][j] holds True if i --> j is a palindrome and False if not
        #only half the arary need to be used since i < j doesnt make sense
        #Base cases are cells[i][i] = True
        #A palindrome is a palindrome if first and last letters are the same and if the interior letters are the same.
        #So, if cells[i-1][j-1] is a palindrome and s[i] == s[j], then it is a palindrome.
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        
        cells = [[False] * len(s) for _ in range(len(s))]

        #Base cases of single letters are true:
        for i in range(len(s)):
            cells[i][i] = True

        windowSize = 1
        #FIXED: urrently calculating like substrings, must calculate all 2 letter cases, then 3, etc. etc. 
        for windowSize in range(1, len(s)):
            #Start at the 2 letter case
            for i in range(len(s)):
                j = i + windowSize
                if j >= len(s):
                    break
                    #Same letter at beginning and end and only 2 letters:
                if s[i] == s[j]:
                    if i == j - 1:
                        cells[i][j] = True
                    #First and last are equal, check middle
                    else:
                        cells[i][j] = cells[i + 1][j - 1]
                #first and last unequal
                else:
                    cells[i][j] = False

        #Longest would be closest to the top right since top right means start at 0, end at end
        #This is min i max j, I don't think we can keep this in a counter? Since a min i might miss a higher interval of j? I guess we could calculate the interval each time and then maximize the interval. Asymptotically this should be the same as searching the space for a max interval at the end so I'm just gonna search for now.
        #check [0,5], then [0,4], [1,5], then [0,3], [1,4], [2,5]
        for i in range(len(s), 0, -1):
            for j in range(0, len(s) - i):
                if cells[j][i + j]:
                    return s[j:i+j+1]
                
        return s[0]
