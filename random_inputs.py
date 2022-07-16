import random
import string


def randomString(length: int = 5) -> str:
    return ''.join(
        random.choice(string.ascii_lowercase) for _ in range(length))


def randomLowerCaseStrings(num_strs: int = 15,
                           min_str_len: int = 2,
                           max_str_len: int = 20) -> list[str]:
    return [
        ''.join(
            random.choice(string.ascii_lowercase)
            for __ in range(random.randint(min_str_len, max_str_len)))
        for _ in range(num_strs)
    ]


def randomUpperCaseStrings(num_strs: int = 15,
                           min_str_len: int = 2,
                           max_str_len: int = 20) -> list[str]:
    return [
        ''.join(
            random.choice(string.ascii_uppercase)
            for __ in range(random.randint(min_str_len, max_str_len)))
        for _ in range(num_strs)
    ]


def randomUpperAndLowerStrings(num_strs: int = 15,
                               min_str_len: int = 2,
                               max_str_len: int = 20) -> list[str]:

    return [
        ''.join(
            random.choice(string.ascii_letters)
            for __ in range(random.randint(min_str_len, max_str_len)))
        for _ in range(num_strs)
    ]


def randomIntArray(low: int = 0,
                   high: int = 20,
                   length: int = 15,
                   ordered=False,
                   increasing=True,
                   allow_duplicates=True) -> list[int]:
    '''
    Generates a random integer array
    ----
    @param low: minimum value, inclusive
    @param high: maximum value, inclusive
    @param length: number of items
    @param ordered: whether the list should be ordered. 
                    If enabled, defaults to increasing
    @param increasing: True for increasing sequence, Fasle for decreasing sequence
                    Ignored if ordered is set to False
    @param allow_duplicates: whether duplicates is allowed
    '''

    raw = [random.choice(range(low, high + 1)) for _ in range(length)]
    if ordered:
        raw.sort(reverse=not increasing)
    if not allow_duplicates:
        return sorted(list(set(raw)))
    return raw


if __name__ == '__main__':
    # print(randomString(), '\n')
    # print(randomLowerCaseStrings(), '\n')
    # print(randomUpperCaseStrings(), '\n')
    # print(randomUpperAndLowerStrings(), '\n')
    print(randomIntArray(length=5, ordered=True), '\n')
    print(randomIntArray(length=5, ordered=True), '\n')