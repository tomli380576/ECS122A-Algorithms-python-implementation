import math


def LIS(arr: list[int], curr_seq: list) -> int:
    if len(arr) == 0:
        return len(curr_seq)

    best = 0
    prev = curr_seq[len(curr_seq) - 1]
    for idx, elem in enumerate(arr):
        if elem > prev:
            curr_seq.append(elem)
            take = LIS(arr[idx:], curr_seq) + 1
            if take > best:
                best = take
            else:
                curr_seq = curr_seq[:len(curr_seq)]
    return best


if __name__ == '__main__':
    sample_set = [
        3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
    ]
    print(f'Longest Subsequence length: {LIS(sample_set, [-math.inf])}')
