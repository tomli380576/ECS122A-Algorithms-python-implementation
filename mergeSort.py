import typing as T


def sortAscending(x, y): return x < y
def sortDescending(x, y): return x > y


def merge2SortedArrays(arr1, arr2, predicate) -> list:
    ptr1, ptr2 = 0, 0
    out = []
    while ptr1 != len(arr1) and ptr2 != len(arr2):
        if predicate(arr1[ptr1], arr2[ptr2]):
            out.append(arr1[ptr1])
            ptr1 += 1
        else:
            out.append(arr2[ptr2])
            ptr2 += 1

    out += arr1[ptr1: len(arr1)]
    out += arr2[ptr2: len(arr2)]
    return out


def mergeSort(arr: list, predicate: T.Callable[[T.Any, T.Any], bool]) -> list:
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr[0]]
    if len(arr) == 2:
        if predicate(arr[0], arr[1]):
            return arr
        else:
            return list(reversed(arr))

    middle = len(arr) // 2
    left = mergeSort(arr[0:middle], predicate)
    right = mergeSort(arr[middle: len(arr)], predicate)
    return merge2SortedArrays(left, right, predicate)


if __name__ == '__main__':
    sample_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5,
                  3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
    print(f'Original: {sample_arr}')
    print(f'Sorted:   {mergeSort(sample_arr, sortDescending)}')
