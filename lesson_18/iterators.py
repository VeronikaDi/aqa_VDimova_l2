from typing import List, Iterator


class ReverseElementsIterator(Iterator):

    __iterable: int

    def __init__(self, iterable: List[int]) -> None:
        self.__iterable = iterable
        self.__index = len(iterable) - 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.__index < 0:
            raise StopIteration
        value = self.__iterable[self.__index]
        self.__index -= 1
        return value


class ReturnsEvenNumbersIterator(Iterator):

    __N: int

    def __init__(self, N: int) -> None:
        self.__number = N
        self.__current = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.__current > self.__number:
            raise StopIteration
        current = self.__current
        self.__current += 2
        return current
