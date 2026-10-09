import pytest
import calculator


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0


def test_subtract():
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == -5


def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10
    assert calculator.multiply(0, 100) == 0


def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)