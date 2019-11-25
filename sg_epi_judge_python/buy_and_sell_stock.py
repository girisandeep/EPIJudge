from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    if len(prices) < 2:
        return 0
    
    # 10, 12, 30, 5, 26
    current_buy = prices[0]
    max_profit = 0
    for p in prices[1:]:
    # while i < len(prices):
        # p = prices[i]
        if p < current_buy:
            current_buy = p
        else:
            current_profit = p - current_buy
            if current_profit > max_profit:
                max_profit = current_profit
        # i += 1
    return max_profit

def main():
    print(buy_and_sell_stock_once([17.3, 22.3,17.4, 23.0]))

if __name__ == '__main__':
    # main()
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
