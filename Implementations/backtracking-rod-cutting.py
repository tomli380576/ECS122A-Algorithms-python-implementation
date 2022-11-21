def CutRod(PRICES: list[int], rod_len: int) -> int:
    if rod_len == 0:
        return 0
    if rod_len == 1:
        return PRICES[0]

    best = 0
    for i in range(1, rod_len + 1):
        cut_profit = CutRod(PRICES, rod_len - i) + PRICES[i - 1]
        best = max(best, cut_profit)

    return best


if __name__ == "__main__":
    sample_prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(f"Max profit: {CutRod(sample_prices, len(sample_prices))}")
