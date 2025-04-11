# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        price_prev = prices[0]
        profit = 0
        for day in range(1,len(prices)):
            if prices[day] < price_prev:
                    profit += (price_prev-min_price)
                    min_price = prices[day]             
            elif day+1 == len(prices) and prices[day] > min_price:
                profit += (prices[day]-min_price)

            if prices[day] < min_price :
                min_price = prices[day]               
            price_prev = prices[day]
        return profit


case_1 = Solution()
print(case_1.maxProfit([7,1,5,3,6,4]))
print(case_1.maxProfit([1,2,3,4,5]))
print(case_1.maxProfit([7,6,4,3,1]))
print(case_1.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9]))
