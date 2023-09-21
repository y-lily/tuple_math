from tuple_math import sub


class TestSub:

    def test_returns_difference(self) -> None:
        assert sub((1, 2), (3, 4)) == (-2, -2)

    def test_returns_longest(self) -> None:
        assert sub((1, 2), (3, 4, 5)) == (-2, -2, -5)

    def test_readme_examples(self) -> None:
        assert sub((1, 3), (2, 4)) == (-1, -1)
        assert sub((1, 3, 5), (2, 4)) == (-1, -1, 5)
        assert sub((1, 3), (2, 4, 6)) == (-1, -1, -6)
