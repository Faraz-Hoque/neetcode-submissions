class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Setting two pointers
        l,r = 0,1 #left=buy, right=sell
        maxP = 0

        while r < len(prices):
            #check if profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            # else:  #if not profitable
            #     l += 1  # check next day
            #But this is a bug since we got the lowest price 
            #on the right, we don't need to shift the
            # left pointer to next day but rather shift
            # to the day of lowest price

            else:  #if right price lower
                l = r #shift left pointer all the way to the lowest price on the right
            r += 1   #increment right pointer to next day

        return maxP