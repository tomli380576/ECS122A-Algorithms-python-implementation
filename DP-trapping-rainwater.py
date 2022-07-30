from random_inputs import randomIntArray


def trapRainwater_BruteForce(heights: list[int]) -> int:
    N = len(heights)
    if N < 3:
        return 0

    total_rainwater = 0
    for idx, height in enumerate(heights):
        total_rainwater += min(max(heights[0:idx + 1]), max(
            heights[idx:N])) - height

    return total_rainwater


def trapRainwater_LinearDP(heights: list[int]) -> int:
    N = len(heights)

    if N < 3:
        return 0

    # preallocation
    left_max = [0 for _ in range(N)]
    right_max = [0 for _ in range(N)]

    # Base case: max(height[0], height[1])
    left_max[1] = max(heights[:2])
    for end in range(1, N - 2):
        left_max[end + 1] = max(left_max[end], heights[end + 1])

    right_max[N - 2] = max(heights[N - 2:])
    for start in range(N - 3, 0, -1):
        right_max[start] = max(right_max[start + 1], heights[start])

    total_rainwater = 0
    for idx, curr_height in enumerate(heights[1:N - 1]):
        total_rainwater += min(left_max[idx + 1],
                               right_max[idx + 1]) - curr_height

    return total_rainwater


if __name__ == '__main__':
    input1 = [4, 2, 0, 3, 2, 5]
    input2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    really_large_input = list(range(1500))
    super_large_input = randomIntArray(high=5, length=15000)

    print(
        f'The total rainwater is: {trapRainwater_LinearDP(super_large_input)}')

    # Really slow, do not run it with input size > 100
    # print(
    #     f'The total rainwater is: {trapRainwater_BruteForce(input2)}'
    # )
