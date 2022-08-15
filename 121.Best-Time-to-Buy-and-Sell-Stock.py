# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# def maxProfit(prices):
#     if len(prices) <= 1:
#     return 0
#     diff = []
#     for j in range(len(prices)):
#         currMin = prices[j]
#         for i in range(j+1, len(prices)):
#             currMax = prices[i]
#             diff.append(currMax - currMin)
#     if max(diff) > 0:
#         return max(diff)
#     else:
#         return 0
#去你妈的众所周知 double for loop过不了LeetCode submission

def maxProfit(prices):
    currBuy = prices[0]
    currSell = prices[0]
    diff = []
    diff.append(currSell-currBuy)

    for i in range(1, len(prices)):
        if prices[i] < currBuy:
            currBuy = prices[i]
        else:
            currSell = prices[i]
            diff.append(currSell-currBuy)
    return max(diff)


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1]))