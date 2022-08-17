from math import floor, inf
from time import time
import numpy as np


def FibRecursive(n):
    if n <= 1:
        return n
    return FibRecursive(n - 1) + FibRecursive(n - 2)


# basic DP version
def FibIterative(n):
    f_n_minus_2 = 0
    f_n_minus_1 = 1
    for _ in range(n):
        f_n = f_n_minus_1 + f_n_minus_2
        f_n_minus_2, f_n_minus_1 = f_n_minus_1, f_n
    return f_n_minus_2


def FibMatrixMult(n):
    fib_matrix = np.array([[0, 1], [1, 1]])
    # tells numpy to not use C types but to use python native types
    # Avoids integer overflow
    result_mat = np.array([[0, 1], [1, 1]], dtype=object)

    for _ in range(n):
        result_mat = np.matmul(fib_matrix, result_mat)
    return result_mat[0, 0]


def FibMatrix_RepeatedSquaring(n):
    if n == 0 or n == 1:
        return 1

    fib_matrix = np.array([[0, 1], [1, 1]])
    result_mat = np.array([[0, 1], [1, 1]], dtype=object)

    # Handle the offset. Suppose n=6, then we can only reach 4 by squares
    # The extra 2 steps need to be done through direct iteration
    max_reachable_by_squares = 2**floor(np.log2(n))
    for _ in range(floor(np.log2(n))):
        result_mat = np.matmul(result_mat, result_mat)

    if max_reachable_by_squares < n:
        for _ in range(max_reachable_by_squares, n + 1):
            result_mat = np.matmul(fib_matrix, result_mat)
    return result_mat[0, 0]


def FibMatrix_AdditionChain(n, addition_chain: list[int]):
    assert (addition_chain[len(addition_chain) - 1] == n)

    fib_matrix = np.array([[0, 1], [1, 1]], dtype=object)
    prev_results = {}
    prev_results[1] = fib_matrix

    for idx, exponent in enumerate(addition_chain):
        if idx == 0:
            continue
        # Find the 2 previous exponents that add up to the current one
        exp1, exp2 = TwoSum(addition_chain[:idx], exponent)
        result_mat = np.matmul(prev_results[exp1], prev_results[exp2])
        prev_results[exponent] = result_mat

    return prev_results[n][0, 1]


# O(N)
def TwoSum(arr, target) -> tuple[int, int]:
    pairs = {}
    for elem in arr:
        pairs[elem] = target - elem
    for elem in arr:
        if pairs[elem] in pairs:
            return (elem, pairs[elem])
    return (-1, -1)


if __name__ == '__main__':

    n = 1023

    # Really slow, don't run this one for large values
    t1 = inf
    if n <= 10:
        start = time()
        FibRecursive(n)
        end = time()
        t1 = end - start
        print(f'Recursive: {end-start}s')
    else:
        print(f'n={n} is too big for raw recursion')

    start = time()
    answer = FibIterative(n)
    end = time()
    t2 = end - start
    print(f'Iterative: {end-start}s')

    start = time()
    ans_mat = FibMatrixMult(n)
    end = time()
    assert (ans_mat == answer)
    t3 = end - start
    print(f'Matrix Raw: {end-start}s')

    start = time()
    ans_mat = FibMatrix_RepeatedSquaring(n)
    end = time()
    assert (ans_mat == answer)
    t4 = end - start
    print(f'Matrix Repeated Squaring: {end-start}s')

    # addition_chain = [1, 2, 3, 5, 10, 15, 25, 50, 75, 125, 250, 500, 1000]
    addition_chain = [1, 2, 3, 4, 7, 14, 17, 31, 62, 124, 248, 496, 527, 1023]
    start = time()
    ans_mat = FibMatrix_AdditionChain(n, addition_chain)
    end = time()
    assert (ans_mat == answer)
    t5 = end - start
    print(f'Matrix addition chain: {end-start}s')

    time_dict = {
        'recursive': t1,
        'iterative': t2,
        'matraw': t3,
        'mat_repeated_squares': t4,
        'mat_addition_chain': t5
    }

    print('\nRanked by Time:')
    print(
        list({
            k: v
            for k, v in sorted(time_dict.items(), key=lambda item: item[1])
        }.keys()))
