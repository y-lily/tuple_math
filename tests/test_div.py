import pytest

from tuple_math import div


class TestDiv:

    def test_returns_ratio(self) -> None:
        assert div((5, 10), (2, 5)) == (2.5, 2)

    def test_returns_shortest(self) -> None:
        assert div((5, 10, 20), (2, 5)) == (2.5, 2)

    def test_raises_zero_division_error(self) -> None:
        with pytest.raises(ZeroDivisionError):
            div((5, 10), (2, 0))
