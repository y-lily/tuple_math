import math
from itertools import zip_longest
from typing import Any, Iterable, TypeAlias, TypeVar, overload

_TupleObject = TypeVar("_TupleObject")
pair: TypeAlias = tuple[_TupleObject, _TupleObject]
triple: TypeAlias = tuple[_TupleObject, _TupleObject, _TupleObject]
quadruple: TypeAlias = tuple[_TupleObject,
                             _TupleObject, _TupleObject, _TupleObject]
T = TypeVar("T", bound=float)


@overload
def add(*tuples: pair[T]) -> pair[T]: ...
@overload
def add(*tuples: triple[T]) -> triple[T]: ...
@overload
def add(*tuples: quadruple[T]) -> quadruple[T]: ...
@overload
def add(*tuples: tuple[T, ...]) -> tuple[T, ...]: ...


def add(*tuples: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(sum(x) for x in zip_longest(*tuples, fillvalue=0))


@overload
def sub(first: pair[T], second: pair[T]) -> pair[T]: ...
@overload
def sub(first: triple[T], second: triple[T]) -> triple[T]: ...
@overload
def sub(first: quadruple[T], second: quadruple[T]) -> quadruple[T]: ...
@overload
def sub(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]: ...


def sub(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(x - y for x, y in zip_longest(first, second, fillvalue=0))


@overload
def mult(first: pair[T], second: pair[T]) -> pair[T]: ...
@overload
def mult(first: triple[T], second: triple[T]) -> triple[T]: ...
@overload
def mult(first: quadruple[T], second: quadruple[T]) -> quadruple[T]: ...
@overload
def mult(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]: ...


def mult(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(x * y for x, y in zip(first, second))


@overload
def div(first: pair[T], second: pair[T]) -> pair[float]: ...
@overload
def div(first: triple[T], second: triple[T]) -> triple[float]: ...
@overload
def div(first: quadruple[T], second: quadruple[T]) -> quadruple[float]: ...
@overload
def div(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[float, ...]: ...


def div(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[float, ...]:
    return tuple(x / y for x, y in zip(first, second))


@overload
def floor_div(first: pair[T], second: pair[T]) -> pair[int]: ...
@overload
def floor_div(first: triple[T], second: triple[T]) -> triple[int]: ...
@overload
def floor_div(first: quadruple[T], second: quadruple[T]) -> quadruple[int]: ...


@overload
def floor_div(first: tuple[T, ...],
              second: tuple[T, ...]) -> tuple[int, ...]: ...


def floor_div(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[int, ...]:
    return tuple(x // y for x, y in zip(first, second))


@overload
def mod(first: pair[T], second: pair[T]) -> pair[T]: ...
@overload
def mod(first: triple[T], second: triple[T]) -> triple[T]: ...
@overload
def mod(first: quadruple[T], second: quadruple[T]) -> quadruple[T]: ...
@overload
def mod(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]: ...


def mod(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(x % y for x, y in zip(first, second))


@overload
def round_down_mod(first: pair[T], second: pair[T]) -> pair[T]: ...
@overload
def round_down_mod(first: triple[T], second: triple[T]) -> triple[T]: ...


@overload
def round_down_mod(first: quadruple[T],
                   second: quadruple[T]) -> quadruple[T]: ...


@overload
def round_down_mod(first: tuple[T, ...],
                   second: tuple[T, ...]) -> tuple[T, ...]: ...


def round_down_mod(first: tuple[T, ...], second: tuple[T, ...]) -> tuple[T, ...]:
    """
    NB: This operation does NOT take mod and rounds it down.
    Instead, it rounds the first argument down to the closest factor of the second number.
    E.g., mod_round_down((8,), (3,)) would be equal to (6,), not (2,).
    """
    return tuple(x - x % y for x, y in zip(first, second))


@overload
def max_(*tuples: pair[T]) -> pair[T]: ...
@overload
def max_(*tuples: triple[T]) -> triple[T]: ...
@overload
def max_(*tuples: quadruple[T]) -> quadruple[T]: ...
@overload
def max_(*tuples: tuple[T, ...]) -> tuple[T, ...]: ...


def max_(*tuples: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(max(x) for x in zip_longest(*tuples, fillvalue=-math.inf))


@overload
def min_(*tuples: pair[T]) -> pair[T]: ...
@overload
def min_(*tuples: triple[T]) -> triple[T]: ...
@overload
def min_(*tuples: quadruple[T]) -> quadruple[T]: ...
@overload
def min_(*tuples: tuple[T, ...]) -> tuple[T, ...]: ...


def min_(*tuples: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(min(x) for x in zip_longest(*tuples, fillvalue=-math.inf))


def less(first: tuple[T, ...], second: tuple[T, ...]) -> bool:
    return all(x < y for x, y in zip(first, second))


def less_or_equal(first: tuple[T, ...], second: tuple[T, ...]) -> bool:
    return all(x <= y for x, y in zip(first, second))


@overload
def intify(operand: pair[T]) -> pair[int]: ...
@overload
def intify(operand: triple[T]) -> triple[int]: ...
@overload
def intify(operand: quadruple[T]) -> quadruple[int]: ...
@overload
def intify(operand: tuple[T, ...]) -> tuple[int, ...]: ...


def intify(operand: tuple[T, ...]) -> tuple[int, ...]:
    return tuple(int(x) for x in operand)
