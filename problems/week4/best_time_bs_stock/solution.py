import math


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
    minn, maxx = 0, -math.inf
    max_p = 0
    for idx, val in enumerate(prices):
        if val < minn:
            minn = val
        elif val :
            # calculate the max profit

            pass


if __name__ == '__main__':
    p = [3, 2, 6, 5, 0, 3]
    print(max_profit(p))
