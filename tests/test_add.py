from tuple_math import add


class TestAdd:

    def test_returns_sums(self) -> None:
        assert add((1, 2), (3, 4)) == (4, 6)

    def test_works_with_multiple_tuples(self) -> None:
        assert add((1, 2), (3, 4), (5, 6)) == (9, 12)

    def test_works_with_negative_numbers(self) -> None:
        assert add((1, 2), (-3, -4)) == (-2, -2)

    def test_returns_longest(self) -> None:
        assert add((1, 2), (3, 4, 5)) == (4, 6, 5)

    def test_readme_examples(self) -> None:
        assert add((1, 3), (2, 4)) == (3, 7)
        assert add((1, 3), (2, 4, 6)) == (3, 7, 6)
        assert add((1, 3), (2, 4), (5, 7)) == (8, 14)
