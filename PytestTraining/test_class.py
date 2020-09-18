import pytest


class TestClass:
    def test_one(self):
        x = 'this'
        assert "h" in x

    def test_two(self):
        x = 5
        y = 6
        assert x + y == 11

    def test_three(self):
        x = 'hello'
        assert hasattr(x, "check")
