# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List

def max_profit(prices: List[int]) -> int:
    profit = 0
    for index, buy_price in enumerate(prices):
        for sell_price in prices[index + 1::]:
            if sell_price - buy_price > profit:
                profit = sell_price - buy_price
    return profit


def max_profit2(prices: List[int]) -> int:
    profit = 0
    for index, buy_price in enumerate(prices):
        if index != len(prices) - 1:
            if max(prices[index + 1::]) - buy_price > profit:
                profit = max(prices[index + 1::]) - buy_price
    return profit


print(max_profit([7,1,5,3,6,4]))
print(max_profit2([9,10,5,6,1,8,0]))