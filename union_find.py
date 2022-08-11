from typing import TypeVar, Generic

T = TypeVar('T')


class UnionFind_NaiveArray(Generic[T]):
    container: list[set[T]] = []

    def __init__(self, S: set[T]) -> None:
        for elem in S:
            self.container.append(set([elem]))

    def Find(self, x: T) -> int:
        result_idx = -1

        for idx, set_ in enumerate(self.container):
            if x in set_:
                result_idx = idx

        if result_idx == -1:
            raise ValueError(f'{x} is not one of the elements')

        return result_idx

    def Union(self, x: T, y: T) -> None:
        idx_for_x = -1
        idx_for_y = -1
        for idx, set_ in enumerate(self.container):
            if x in set_:
                idx_for_x = idx
            elif y in set_:
                idx_for_y = idx

        if idx_for_x != -1 and idx_for_y != -1:
            self.container[idx_for_x] = self.container[idx_for_x].union(
                self.container[idx_for_y])
            self.container.pop(idx_for_y)
        else:
            raise ValueError('Either x or y is not in the container')


class UnionFind_ParentPointer(Generic[T]):
    parent: dict[T, T] = {}

    def __init__(self, S: set[T]) -> None:
        for elem in S:
            self.parent[elem] = elem

    def Find(self, x: T) -> T:
        if x not in self.parent:
            raise ValueError(f'{x} is not one of the elements')

        return self.parent[x]

    # I didn't do the full linked list version here
    # If you implement a custom linked list, complexity is O(min(len(x), len(y)))
    # where len(x) is the size of the set that x is in
    # Here complexity is len(y)
    def Union(self, x: T, y: T) -> None:
        for elem, _parent in filter(lambda item: item[1] == self.parent[y],
                           self.parent.items()):
            self.parent[elem] = x


def driverCode1():
    sample_set = set([5, 4, 3, 1, 6, 7, 9])
    union_find = UnionFind_NaiveArray(sample_set)

    print(f'Find(5) returns index: {union_find.Find(5)}')

    print('Now union {5} and {3}')
    union_find.Union(5, 3)
    print(f'Container after union: {union_find.container}')

    print('Now union {4} and {9}')
    union_find.Union(4, 9)
    print(f'Container after union: {union_find.container}')

    print('Try bad inputs')
    try:
        union_find.Find(1000)
    except ValueError as error:
        print(f'bad input, {error}')


def driverCode2():
    union_find = UnionFind_ParentPointer(set([5, 4, 3, 1, 6, 7, 9]))
    print(f'Find(5), parent is: {union_find.Find(5)}')

    print('Now union {5} and {3}')
    union_find.Union(5, 3)
    print(f'Container after union: {union_find.parent}')
    print(f'Find(5) = {union_find.Find(5)}, Find(3) = {union_find.Find(3)}')

    print('Now union {4} and {9}')
    union_find.Union(4, 9)
    print(f'Container after union: {union_find.parent}')

    print('Try bad inputs')
    try:
        union_find.Find(1000)
    except ValueError as error:
        print(f'bad input, {error}')


if __name__ == '__main__':
    driverCode2()