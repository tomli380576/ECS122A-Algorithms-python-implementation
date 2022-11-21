from math import inf


def MaxMiddleSum(arr: list[int], low: int, mid: int, high: int) -> int:
    best_left_sum = -inf
    curr_sum = 0

    # Has to go reversed to the left because the final array has to be contiguous
    for i in reversed(range(low, mid)):
        curr_sum += arr[i]
        if curr_sum > best_left_sum:
            best_left_sum = curr_sum

    best_right_sum = -inf
    curr_sum = 0

    # has to go in the normal order
    for i in range(mid, high + 1):
        curr_sum += arr[i]
        if curr_sum > best_right_sum:
            best_right_sum = curr_sum

    # the type:ignores are just there so the linter doesn't complain about adding a float to an int
    return max(
        best_left_sum + best_right_sum,  # type: ignore
        best_left_sum,  # type: ignore
        best_right_sum,
    )  # type: ignore


def MaxSubarray(arr: list[int], low: int, high: int) -> int:
    if len(arr) == 0:
        raise ValueError("arr cannot be empty")

    if low == high:
        return arr[0]

    middle = (high + low) // 2

    result_left = MaxSubarray(arr, low, middle)
    result_right = MaxSubarray(arr, middle + 1, high)
    result_mid = MaxMiddleSum(arr, low, middle, high)
    return max(result_left, result_mid, result_right)


if __name__ == "__main__":
    testarr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(
        f"Max subarray sum for {testarr} is {MaxSubarray(testarr, 0, len(testarr) - 1)}"
    )
