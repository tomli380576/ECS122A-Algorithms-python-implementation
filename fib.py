from math import floor
from time import time
import numpy as np

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    f_n_minus_2 = 0
    f_n_minus_1 = 1
    for i in range(n):
        f_n = f_n_minus_1 + f_n_minus_2
        f_n_minus_2, f_n_minus_1 = f_n_minus_1, f_n
    return f_n_minus_2


def fib_matrix_mult(n):
    fib_matrix = np.array([[0, 1], [1, 1]])
    result_mat = np.array([[0, 1], [1, 1]])

    for _ in range(n):
        result_mat = np.matmul(fib_matrix, result_mat)
    return result_mat[0, 1]


def fib_matrix_repeated_squaring(n):
    if n == 0 or n == 1:
        return 1

    fib_matrix = np.array([[0, 1], [1, 1]])
    result_mat = np.array([[0, 1], [1, 1]])

    # Handle the offset. Suppose n=6, then we can only reach 4 by squares
    # The extra 2 steps need to be done through direct iteration
    max_reachable_by_squares = 2**floor(np.log2(n))
    for _ in range(floor(np.log2(n))):
        result_mat = np.matmul(result_mat, result_mat)

    if max_reachable_by_squares < n:
        for _ in range(max_reachable_by_squares, n):
            result_mat = np.matmul(fib_matrix, result_mat)
    return result_mat[0, 1]


def fib_matrix_addition_chain(n, addition_chain: list[int]):
    assert (addition_chain[len(addition_chain) - 1] == n)

    fib_matrix = np.array([[0, 1], [1, 1]])
    prev_results = {}
    prev_results[1] = fib_matrix

    for idx, exponent in enumerate(addition_chain):
        if idx == 0:
            continue
        exp1, exp2 = twoSum(addition_chain[:idx], exponent)
        result_mat = np.matmul(prev_results[exp1], prev_results[exp2])
        prev_results[exponent] = result_mat

    return prev_results[n][0, 1]


# O(N)
def twoSum(arr, target) -> tuple[int, int]:
    pairs = {}
    for elem in arr:
        pairs[elem] = target - elem
    for elem in arr:
        if pairs[elem] in pairs:
            return (elem, pairs[elem])
    return (-1, -1)


if __name__ == '__main__':

    n = 30

    start = time()
    fib_recursive(n)
    end = time()
    t1 = end - start
    print(f'Recursive: {end-start}s')

    start = time()
    fib_iterative(n)
    end = time()
    t2 = end - start
    print(f'Iterative: {end-start}s')

    start = time()
    fib_matrix_mult(n)
    end = time()
    t3 = end - start
    print(f'Matrix Raw: {end-start}s')

    start = time()
    fib_matrix_repeated_squaring(n)
    end = time()
    t4 = end - start
    print(f'Matrix Repeated Squaring: {end-start}s')

    addition_chain_100 = [1, 2, 3, 5, 10, 15, 30]
    start = time()
    fib_matrix_addition_chain(n, addition_chain_100)
    end = time()
    t5 = end - start
    print(f'Matrix addition chain: {end-start}s')

    timedict = {
        'recursive': t1,
        'iterative': t2,
        'matraw': t3,
        'mat_repeated_squares': t4,
        'mat_addition_chain': t5
    }


    print('Ranked by Time:')
    print(list({k: v for k, v in sorted(timedict.items(), key=lambda item: item[1])}.keys()))
