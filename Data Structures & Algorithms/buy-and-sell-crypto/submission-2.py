class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_sell = 0
        sell_price = []
        for i in range(len(prices)-1, -1, -1):
            highest_sell = max(highest_sell, prices[i])
            sell_price.append(highest_sell)
        sell_price = sell_price[::-1]
        print(sell_price)

        lowest_buy = max(prices)
        buy_price = []

        for i in range(len(prices)):
            lowest_buy = min(lowest_buy, prices[i])
            buy_price.append(lowest_buy)
        print(buy_price)

        profits = []
        for buy, sell in zip(buy_price, sell_price):
            profit = sell - buy
            profits.append(profit)
        print(profits)
        
        return 0 if max(profits) < 0 else max(profits)



        # return sell_price