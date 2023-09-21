import pytest
from pytest import approx

from tuple_math import mod


class TestMod:

    def test_returns_remainder(self) -> None:
        assert mod((4, 5), (3, 2)) == (1, 1)

    def test_works_with_fractions(self) -> None:
        assert mod((3.1, 5.5), (3, 2)) == (approx(0.1), approx(1.5))

    def test_returns_shortest(self) -> None:
        assert mod((4, 5), (3, 2, 1)) == (1, 1)

    def test_raises_zero_division_error(self) -> None:
        with pytest.raises(ZeroDivisionError):
            mod((4, 5), (3, 0))
