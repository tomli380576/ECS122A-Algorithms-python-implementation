import errno
from typing import TypeVar, Generic
from abc import ABCMeta

T = TypeVar("T")


# Abstract Base Class / Interface
class UnionFind(Generic[T], metaclass=ABCMeta):
    def __init__(self, S: set[T]) -> None:
        ...

    def Find(self, x: T) -> int:
        ...

    def Union(self, x: T, y: T) -> None:
        ...

    def GetContainerStr(self) -> str:
        ...

    pass


class NaiveArrayUF(UnionFind, Generic[T]):
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
            raise ValueError(f"{x} is not one of the elements")

        return result_idx

    def Union(self, x: T, y: T) -> None:
        if x == y:
            return

        idx_for_x = -1
        idx_for_y = -1
        for idx, set_ in enumerate(self.container):
            if x in set_:
                idx_for_x = idx
            elif y in set_:
                idx_for_y = idx

        if idx_for_x != -1 and idx_for_y != -1:
            self.container[idx_for_x] = self.container[idx_for_x].union(
                self.container[idx_for_y]
            )
            self.container.pop(idx_for_y)
        else:
            raise ValueError("Either x or y is not in the container")

    def GetContainerStr(self) -> str:
        return str(self.container)


class ParentPointerUF(UnionFind, Generic[T]):
    parent: dict[T, T] = {}

    def __init__(self, S: set[T]) -> None:
        for elem in S:
            self.parent[elem] = elem

    def Find(self, x: T) -> T:
        try:
            return self.parent[x]
        except KeyError:
            raise ValueError(f"{x} is not one of the elements")

    # I didn't do the full linked list version here
    # If you implement a custom linked list, complexity is O(min(len(x), len(y)))
    # where len(x) is the size of the set that x is in
    # Here complexity is len(set that has y)
    def Union(self, x: T, y: T) -> None:
        if x == y:
            return
        try:
            self.parent[x]
        except KeyError:
            raise ValueError(f"{x} is not one of the elements")
        try:
            self.parent[y]
        except KeyError:
            raise ValueError(f"{y} is not one of the elements")

        for elem, _parent in filter(
            lambda item: item[1] == self.parent[y], self.parent.items()
        ):
            self.parent[elem] = x

    def GetContainerStr(self) -> str:
        return str(self.parent)


def sampleDriverCode():

    uf_pointer = ParentPointerUF(set([5, 4, 3, 1, 6, 7, 9]))
    uf_array = NaiveArrayUF(set([5, 4, 3, 1, 6, 7, 9]))
    print(f"uf_pointer Find(5), parent is: {uf_pointer.Find(5)}")
    print(f"uf_array Find(5) returns index: {uf_array.Find(5)}")

    print("\nNow union {5} and {3}")
    uf_pointer.Union(5, 3)
    uf_array.Union(5, 3)

    print(f"\nuf_pointer Container after union: {uf_pointer.GetContainerStr()}")
    print(f"uf_array Container after union: {uf_array.GetContainerStr()}")

    print(
        f"\nuf_pointer Find(5) = {uf_pointer.Find(5)}, Find(3) = {uf_pointer.Find(3)}"
    )
    print(f"uf_array Find(5) = {uf_array.Find(5)}, Find(3) = {uf_array.Find(3)}")

    print("\nNow union {4} and {9}")
    uf_pointer.Union(4, 9)
    uf_array.Union(4, 9)

    print(f"\nuf_pointer Container after union: {uf_pointer.GetContainerStr()}")
    print(f"uf_array Container after union: {uf_array.GetContainerStr()}")

    print("\nTry bad inputs")
    try:
        uf_pointer.Find(1000)
    except ValueError as error:
        print(f"bad input in uf_pointer, {error}")

    try:
        uf_array.Find(1000)
    except ValueError as error:
        print(f"bad input in uf_array, {error}")


def randomDriverCode():
    from random_inputs import randomIntArray
    from random import randint

    # calling the set constructor will remove duplicates
    # here we are setting the allow_duplicates to actually get num_elem amount of elements
    num_elems = randint(5, 20)
    min_val = randint(-100, 0)
    max_val = randint(min_val + num_elems, min_val + num_elems * 2)
    rand_set = set(
        randomIntArray(
            low=min_val, high=max_val, length=num_elems, allow_duplicates=False
        )
    )

    valid_uf_choices = set(["p", "a"])
    union_find = ParentPointerUF(rand_set)
    uf_choice = input(
        "Choose UnionFind Implementation: (A)rray, (P)arent Pointer "
    ).lower()
    while uf_choice not in valid_uf_choices:
        uf_choice = input(
            "Invalid Choice. Choose UnionFind Implementation: (A)rray, (P)arent Pointer "
        )

    if uf_choice == "p":
        union_find = ParentPointerUF(rand_set)
    if uf_choice == "a":
        union_find = NaiveArrayUF(rand_set)

    valid_operations = set(["f", "u", "p", "s"])
    while True:
        operation = input(
            "Choose Operation: (F)ind, (U)nion, (P)rint Container, (S)top "
        ).lower()
        while operation not in valid_operations:
            operation = input(
                "Invalid Choice. Choose Operation: (F)ind, (U)nion, (P)rint Container, (S)top "
            ).lower()

        if operation == "s":
            exit(0)

        if operation == "f":
            num_to_find = randint(-100, 100)
            print(f"Trying to find: {num_to_find}")
            idx = 0
            try:
                idx = union_find.Find(num_to_find)
            except ValueError as e:
                print(e)
            else:
                print(f"Found at index: {idx}") if uf_choice == "a" else print(
                    f"Found parent: {idx}"
                )
                print(f"Container: {union_find.GetContainerStr()}")

        if operation == "u":
            x = randint(min_val, max_val)
            y = randint(min_val, max_val)
            print(f"Trying to union: {x}, {y}")
            try:
                union_find.Union(x, y)
            except ValueError as e:
                print(e)
            else:
                print(f"Container: {union_find.GetContainerStr()}")

        if operation == "p":
            print(f"Container: {union_find.GetContainerStr()}")


if __name__ == "__main__":
    randomDriverCode()
