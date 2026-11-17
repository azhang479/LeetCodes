class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #Using US currency, we can just continuously subtract the largest coin
        #This doesnt necessarily always work?
        #[1, 2, 70, 100] coins, 140 can be made with 2 70 coins, using a 100 coin would make it a lot more than 2 coins.
        #dp[i]: using the first i coins, what is the best combination to make amount?
        
        #dp has [1xn], each i is min coins to make i, found by min(dp[i - each coin]) + 1
        #base case is all the coins
        if amount == 0:
            return 0
        
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0
        #If the coin can make the exact change, then it is possible. Else, it is infinite since we're doing min
        for coin in coins:
            if coin < len(amounts):
                if coin % amount == 0:
                    amounts[coin] = coin // amount

        for i in range(1, len(amounts)):
            for coin in coins:
                currCheck = i - coin
                #If coin is out of bounds, dont check
                if currCheck < 0 or currCheck >= len(amounts):
                    continue
                amounts[i] = min(amounts[i], amounts[currCheck]) #find the minimum number
            if amounts[i] != float('inf'):
                amounts[i] += 1 #add this 1 coin 
        
        if amounts[-1] == float('inf'):
            return -1
        return amounts[-1]
                
