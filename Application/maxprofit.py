
def findMaxProfit1(prices) :
    n = len(prices)
    max_profit = 0

    for i in range(n - 1) :
        for j in range(i + 1, n) :
            profit = prices[j] - prices[i]

            if profit > max_profit :
                max_profit = profit

    return max_profit

def findMaxProfit2(prices) :
    n = len(prices)
    min_price = prices[0]
    max_profit = 0

    for i in range(1, n) :
        profit = prices[i] - min_price

        if profit > max_profit :
            max_profit = profit

        if prices[i] < min_price :
            min_price = prices[i]

    return max_profit

prices = [10300, 9200, 10000, 9000, 8900, 9500, 9300]

print(findMaxProfit1(prices))
print(findMaxProfit2(prices))