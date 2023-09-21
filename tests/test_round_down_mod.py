import pytest
from pytest import approx

from tuple_math import round_down_mod


class TestRoundDownMod:

    def test_rounds_down_to_closest_factor(self) -> None:
        assert round_down_mod((8, 9), (3, 4)) == (6, 8)

    def test_works_with_fractions(self) -> None:
        assert round_down_mod((8, 9), (3.4, 4.2)) == (approx(6.8), approx(8.4))

    def test_returns_shortest(self) -> None:
        assert round_down_mod((3, 4), (1, 2, 3)) == (3, 4)

    def test_raises_zero_division_error(self) -> None:
        with pytest.raises(ZeroDivisionError):
            round_down_mod((5, 9), (2, 0))

    def test_readme_examples(self) -> None:
        assert round_down_mod((8,), (3,)) == (6,)
        assert round_down_mod((6, 8, 9), (4, 3, 3)) == (4, 6, 9)
