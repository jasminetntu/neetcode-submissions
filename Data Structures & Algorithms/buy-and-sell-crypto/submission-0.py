class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # keep track of max profit

        # start from left
        # while right < len
        #   if curr > max, update max
        #   if left + 1 = right, inc right # WRONG!!!
        #   if sum of left + 1 > sum of right + 1, inc left; else inc right



        max_profit = 0

        b = 0
        s = 1
        min = prices[b]

        while b < s and s < len(prices):
            if prices[s] - prices[b] > max_profit:
                max_profit = prices[s] - prices[b]

            if prices[s] < min:
                min = prices[s]
                b = s
                s = b + 1
            else:
                s += 1
            


        return max_profit
