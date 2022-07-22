import random
import string


def randomString(letters: str = string.ascii_lowercase,
                 length: int = 5) -> str:
    return ''.join(random.choice(letters) for _ in range(length))


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


def randomIntArray(low: int = -20,
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
                    *Ignored if ordered == False*
    @param allow_duplicates: whether duplicates is allowed
    '''
    if high - low + 1 < length and not allow_duplicates:
        raise ValueError(
            f'Cannot generate list with more than {high-low+1} unique numbers in [{low}, {high}]'
        )

    raw = [random.choice(range(low, high + 1)) for _ in range(length)]

    if not allow_duplicates:
        set_raw = set(raw)
        while len(set_raw) < length:
            set_raw.add(random.choice(range(low, high + 1)))
        raw = list(set_raw)

    if ordered:
        raw.sort(reverse=not increasing)

    return raw


def randomLetterArray(length: int = 15,
                      ordered=False,
                      increasing=True,
                      allow_duplicates=True) -> list[str]:
    '''
    Generates a random integer array
    ----
    @param length: number of items
    @param ordered: whether the list should be ordered. 
                    If enabled, defaults to increasing
    @param increasing: True for increasing sequence, Fasle for decreasing sequence
                    *Ignored if ordered == False*
    @param allow_duplicates: whether duplicates is allowed
    '''

    if length > 26 and not allow_duplicates:
        raise ValueError(
            'Cannot generate string with more than 26 unique latin letters')

    raw = [random.choice(string.ascii_uppercase) for _ in range(length)]

    if not allow_duplicates:
        set_raw = set(raw)
        while len(set_raw) < length:
            set_raw.add(random.choice(string.ascii_uppercase))
        raw = list(set_raw)

    if ordered:
        raw.sort(reverse=not increasing)

    return raw


if __name__ == '__main__':
    # print(randomString(), '\n')
    # print(randomLowerCaseStrings(), '\n')
    # print(randomUpperCaseStrings(), '\n')
    # print(randomUpperAndLowerStrings(), '\n')
    print(randomIntArray(length=25, ordered=False), '\n')
    print(randomIntArray(length=25, ordered=False), '\n')
