class Solution:
    def numDecodings(self, s: str) -> int:
        #Each number adds valid decodings, doesn't remove any
        #We can do some kinda DP to decode the message? 
        #dp[i] stores how many ways to decode with characters 0 up to i
        #"11106"
        #"1" has 1 way
        #"11" the 1 has 2 ways (1, 1) or (11)
        #"111" has 3 ways (1, 11) or (11, 1) or (1, 1, 1)
        #"1110" has 2 ways (1, 1, 10), (11, 10) zero removes a way? Since 0 cant be on its own
        #"11106" has 2 ways (1, 1, 10, 6), (11, 10, 6), 
        #111062 has 2 ways (1, 1, 10, 6, 2), (11, 10, 6, 2)
        #1110621 has 4 ways (1, 1, 10, 6, 2, 1), (11, 10, 6, 2, 1), (1, 1, 10, 6, 21), (11, 10, 6, 21)

        #when adding a single digit that is >= 7 and last digit is a 1, it adds 1 way of decoding as it can be singular [7,8,9] or [17,18,19]
        #when adding single digit that is >= 7 and last digit is not a 1, it adds 0 ways of decoding as it must be on its own.
        #when adding single digit that is >= 1, and last digit is a 1 or 2, it adds 1 way of decoding as it can be a 2 digit or a single digit 
        #when adding a single digit that is >= 1 and last digit is not a 1 or 2, it adds 0 ways of decoding
        #When adding a 0, if last 2 digits are 1/2, then it removes a way of decoding
        #When adding a 0, if last digit is a 1 or a 2, then it does nothing
        #when adding 0, if last digit is not a 1 or a 2, it is invalid as 0 must come on the end of a number
        #Adding 0 must mark 0 as next digit must be nonzero or else not a valid code
        #starting from 0 is invalid always
        #not gonna do dp anymore just going to do it with a counter
        if s[0] == "0":
            return 0
        ways = [0] * len(s)
        ways[0] = 1
        for i in range(1, len(s)):
            #If it can be decoded 2 ways, ways = ways[i-1] + ways[i-2]
            if s[i] in ["7", "8", "9"]:
                if s[i-1] == "1":
                    if i == 1:
                        ways[i] = 2
                    else:
                        ways[i] = ways[i-1] + ways[i-2]
                else:
                    ways[i] = ways[i-1]
            elif s[i] in ["1", "2", "3", "4", "5", "6"]:
                if s[i-1] in ["1", "2"]:
                    if i == 1:
                        ways[i] = 2
                    else:
                        ways[i] = ways[i-1] + ways[i-2]
                else:
                    ways[i] = ways[i-1]
            elif s[i] == "0":
                if i == 1:
                    if s[i-1] not in ["1", "2"]:
                        return 0
                    ways[i] = ways[i-1] #on second one, doesnt change the 1 way
                else:
                    if s[i-1] in ["1", "2"] and s[i-2] in ["1", "2"]:
                        ways[i] = ways[i-2] #steals the previous number's added ways, so goes back to i-2
                    elif s[i-1] not in ["1", "2"]:
                        return 0
                    else:
                        ways[i] = ways[i-1]
        print(ways)
        return ways[-1]
                         