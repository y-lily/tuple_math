import pytest

from tuple_math import floor_div


class TestFloorDiv:

    def test_returns_integer_ratio(self) -> None:
        assert floor_div((5, 9), (2, 5)) == (2, 1)

    def test_returns_shortest(self) -> None:
        assert floor_div((5, 9, 8), (2, 5)) == (2, 1)

    def test_raises_zero_division_error(self) -> None:
        with pytest.raises(ZeroDivisionError):
            floor_div((5, 9), (2, 0))
