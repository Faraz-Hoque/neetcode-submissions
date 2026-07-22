class Solution:
    def maxProfit(self, prices):
        buy = prices[0]  #setting 0th day as buying day
        profit = 0  #initializing profit as 0

        #iterating through price list of day 1 to last day
        for i in range(1, len(prices)):
            #setting new profit variable to 
            #store each profit every iteration
            newProfit = prices[i] - buy

            #if lower price of stock found,
            #buy set to that price straight away
            if prices[i] < buy:
                buy = prices[i]
            elif newProfit > profit:
                profit = newProfit
            #if new profit in an iteration is found 
            #greater than current profit, 
            #the current profit is set to the new profit
        return profit