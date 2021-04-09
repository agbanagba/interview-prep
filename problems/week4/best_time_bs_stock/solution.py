def max_profit(prices):
    max_p = 0
    minn = prices[0]
    for idx, val in enumerate(prices):
        if val < minn:
            minn = val
        elif val - minn > max_p:
            max_p = val - minn
    return max_p


def max_profit_2(prices):
    minn, maxx = prices[0], prices[0]
    max_p = 0
    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        minn = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        maxx = prices[i]
        max_p += maxx - minn
    return max_p


def max_profit_2_eff(prices):
    max_p = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_p += prices[i] - prices[i - 1]
    return max_p


def max_profit_3(prices):
    # Dynamic programming problem - oh well
    pass

if __name__ == '__main__':
    p = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(max_profit_3(p))
