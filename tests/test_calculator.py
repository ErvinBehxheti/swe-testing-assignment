import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# --- Addition ---

def test_add_positive_numbers(calc):
    assert calc.add(5, 3) == 8

def test_add_negative_numbers(calc):
    assert calc.add(-4, -6) == -10

def test_add_mixed_sign_numbers(calc):
    assert calc.add(-7, 10) == 3


# --- Subtraction ---

def test_subtract_positive_numbers(calc):
    assert calc.subtract(10, 4) == 6

def test_subtract_resulting_in_negative(calc):
    assert calc.subtract(3, 9) == -6


# --- Multiplication ---

def test_multiply_positive_numbers(calc):
    assert calc.multiply(6, 7) == 42

def test_multiply_by_zero(calc):
    assert calc.multiply(99, 0) == 0

def test_multiply_large_numbers(calc):
    assert calc.multiply(1_000_000, 1_000_000) == 1_000_000_000_000


# --- Division ---

def test_divide_positive_numbers(calc):
    assert calc.divide(10, 2) == 5.0

def test_divide_returns_decimal(calc):
    assert calc.divide(7, 2) == pytest.approx(3.5)

def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

def test_divide_negative_dividend(calc):
    assert calc.divide(-9, 3) == -3.0


# --- Decimal / floating-point edge cases ---

def test_add_decimal_numbers(calc):
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply_decimal_numbers(calc):
    assert calc.multiply(1.5, 4) == pytest.approx(6.0)


# --- Clear ---

def test_clear_resets_result(calc):
    calc.result = 42
    assert calc.clear() == 0

def test_clear_returns_zero_when_already_zero(calc):
    assert calc.clear() == 0
