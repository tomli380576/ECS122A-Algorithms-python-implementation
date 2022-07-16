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
                   length: int = 15) -> list[int]:
    return [random.choice(range(low, high + 1)) for _ in range(length)]


if __name__ == '__main__':
    print(randomString(), '\n')
    print(randomLowerCaseStrings(), '\n')
    print(randomUpperCaseStrings(), '\n')
    print(randomUpperAndLowerStrings(), '\n')
    print(randomIntArray(), '\n')