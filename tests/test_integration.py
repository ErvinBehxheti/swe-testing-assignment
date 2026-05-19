from unittest.mock import patch
import io
import pytest
from main import run


def run_session(inputs):
    """Drive run() with a list of input strings, return captured stdout."""
    with patch("builtins.input", side_effect=inputs + ["quit"]):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
            run()
            return mock_out.getvalue()


# --- Full interaction flows ---

def test_addition_full_flow():
    output = run_session(["5 + 3"])
    assert "Result: 8" in output


def test_subtraction_full_flow():
    output = run_session(["10 - 4"])
    assert "Result: 6" in output


def test_multiplication_full_flow():
    output = run_session(["6 * 7"])
    assert "Result: 42" in output


def test_division_full_flow():
    output = run_session(["9 / 2"])
    assert "Result: 4.5" in output


def test_clear_after_calculation_resets_display():
    output = run_session(["8 * 5", "clear"])
    assert "Result: 0" in output


def test_division_by_zero_shows_error():
    output = run_session(["10 / 0"])
    assert "Error" in output


def test_invalid_operator_shows_error():
    output = run_session(["5 ^ 3"])
    assert "Error" in output


def test_sequential_operations_independent():
    """Each expression is evaluated on its own operands, not accumulated."""
    output = run_session(["2 + 2", "10 - 3"])
    assert "Result: 4" in output
    assert "Result: 7" in output
