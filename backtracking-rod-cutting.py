PRICES = [1, 5, 8, 9, 10, 17, 17, 20]  # sample prices


def cutRod(rod_len) -> int:
    if rod_len == 0:
        return 0
    if rod_len == 1:
        return PRICES[0]

    best = 0
    for i in range(1, rod_len + 1):
        price_if_make_cut = cutRod(rod_len - i) + PRICES[i - 1]
        if price_if_make_cut > best:
            best = price_if_make_cut

    return best