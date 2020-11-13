'''
Your boss at a trading firm wants to analyze the opportunity P&L day trading TSLA for the past 6 months.
He has asked you to write a code that will identify the best trade on any given day, by specifying an entry and exit point, with the following constraints: 
    No holding the security overnight 
    You are not allowed short-selling 
    You have maximum one trade per day 
The price history of TSLA is provided as an array with values indicating the progression of prices from cash open to market close. 
Here is a sample input: [402.46, 399.42, 402., 399.45, 399.66, 400.19, 402.48, 405.60, 405.07] 
Given this input you should output: 
Maximum profit for the day
'''
def find_max_profit(prices):
    minimum_entry_price = prices[0]
    price_diff = []
    for price in prices[1:]:
        price_diff.append(price - minimum_entry_price)
        if minimum_entry_price > price:
            minimum_entry_price = price
    return max(max(price_diff), 0)

prices = [402.46, 399.42, 402., 399.45, 399.66, 400.19, 402.48, 405.60, 405.07]

print(find_max_profit(prices))