from tuple_math import mult


class TestMult:

    def test_returns_product(self) -> None:
        assert mult((1, 2), (3, 4)) == (3, 8)

    def test_returns_shortest(self) -> None:
        assert mult((1, 2, 3), (4, 5)) == (4, 10)

    def test_readme_examples(self) -> None:
        assert mult((1, 3), (2, 4)) == (2, 12)
