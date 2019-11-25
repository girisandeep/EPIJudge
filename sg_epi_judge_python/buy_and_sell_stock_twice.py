from test_framework import generic_test


def buy_and_sell_stock_twice(prices):

    best_two_min_heap = []

    if len(prices) < 2:
        return 0
    
    # 10, 12, 30, 5, 26
    current_buy = prices[0]
    max_profit = 0
    heappush(best_two_min_heap, 0)
    heappush(best_two_min_heap, 0)

    for p in prices[1:]:
    # while i < len(prices):
        # p = prices[i]
        if p < current_buy:
            current_buy = p
        else:
            current_profit = p - current_buy
            if current_profit > best_two_min_heap[0]:
                heappop(best_two_min_heap)
                heappush(best_two_min_heap, current_profit)
            # if current_profit > max_profit:
            #     max_profit = current_profit
        # i += 1
    return sum(best_two_min_heap)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
