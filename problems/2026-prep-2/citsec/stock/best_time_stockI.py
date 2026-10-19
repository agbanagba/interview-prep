
# LC 122. Best Time to buy and sell stock II
def maxProfitII(prices) -> int:

    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maxProfit += prices[i] - prices[i - 1]

    return maxProfit

# Same LC 122 but with a different way of thinking about it. 
def maxProfitII_DP(prices) -> int:

    # We will model it as a state machine
    # At the end of the day, we either want to be holding or not holding. At the end of the prices, the goal is not holding
    # so we will return that. 
    # If we end the day holding:
    #  then a) it means we can just keep holding and not do anything or b) we were not holding from yesterday and we need to buy
    # If we end the day not holding
    #   then a) we can keep not holding from yesterday and do nothing b) we can sell what we have from yesterday

    if not prices:
        return 0

    holding = -prices[0]
    not_holding = 0

    for i in range(1, len(prices)):
        holding = max(holding, not_holding - prices[i])
        not_holding = max(not_holding, holding + prices[i])


    return not_holding

# This is LC 714. best Time to Buy and Sell Stock With Transaction Fee
# The solution applies the fee during the sell. so the initial sell on day 1 
# and on subsequent sell. The fee could also be applied to buying 
def maxProfit714(self, prices: list[int], fee: int) -> int:
    if not prices:
        return 0

    holding = -prices[0] -fee
    not_holding = 0

    for i in range(1, len(prices)):
        holding = max(holding, not_holding - prices[i] - fee)
        not_holding = max(not_holding, holding + prices[i])

    return not_holding


# LC 309: Best Time to Buy and Sell Stock with Cooldown period.
def maxProfit309(prices) -> int:
    if not prices:
        return 0

    # Same idea as the solutions above, we represent this as a state machine
    # But this time, it's 3. Held, Sold and Ready.
    # For held: (This is how we want to end the day)
    #   a) we already holding from yesterday so we keep holding, b) we rested yesterday so we buy.( rested means that we did not buy)
    # For sold:
    #   a) we do nothing as we already sold yesterday. b) we 

    held = -prices[0]
    sold = float('-inf')
    ready = 0

    for i in range(1, len(prices)):
        c_held = max(held, ready - prices[i])
        c_sold = held + prices[i] # the only option here is to sell what we held yesterday. 
        c_ready = max(ready, sold)

        held = c_held
        sold = c_sold
        ready = c_ready

    return max(sold, ready)


# LC 123: Best time to buy and sell stock III
def maxProfit123(prices) -> int:
    if not prices:
        return 0

    # still state machine way of thinking. 
    # 4 way state machine. 
    # prior examples was a simple question each day. holding or not holding (one stock being sold or bought)
    # here its two different stocks. 
    # Stock 1: Am I holding, Am I selling?
    # Same for stock 2

    # State machine
    # t1_held - max profit if we are currently holding our first stock
    # t1_sold - max profit if we sold our first stock
    # t2_held - max profit if we are holding our second stock
    # t2_sold - max profit if we have completed our second sale. 

    if not prices:
        return 0

    t1_held, t2_held = float('-inf'), float('-inf')
    t1_sold, t2_sold = 0, 0

    for price in prices:
        t1_held = max(t1_held, -price)
        t1_sold = max(t1_sold, t1_held + price)
        t2_held = max(t2_held, t1_sold - price)
        t2_sold = max(t2_sold, t2_held + price)

    return t2_sold

# This is for LC 188. Similar to 123, but with k transactions. 
# we just need k variables and track prev_profit each time.
def maxProfit188(k: int, prices: list[int]) -> int:
    if not prices or k == 0:
        return 0

    held = [float('-inf')] * k
    sold = [0] * k

    for price in prices:
        for j in range(k):
            prev_profit = 0 if j == 0 else sold[j - 1]

            held[j] = max(held[j], prev_profit - price)
            sold[j] = max(sold[j], held[j] + price)

    return sold[-1]
