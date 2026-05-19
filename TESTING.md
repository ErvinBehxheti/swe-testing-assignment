# Testing Strategy — Quick-Calc

## 1. Overview of Approach

The testing strategy for Quick-Calc is intentionally layered. The core calculation logic in `calculator.py` is isolated from the input/output layer in `main.py`, which makes it possible to test each concern independently. Unit tests target `Calculator` methods directly, passing values in and asserting on the return value with no I/O involved. Integration tests drive the full CLI session by patching `builtins.input` and capturing `sys.stdout`, verifying that user-facing text reflects the correct computed result.

The test suite is kept entirely automated: `python3 -m pytest -v` runs all 24 tests without any manual steps.

---

## 2. What Was Tested

| Area | What is covered |
|---|---|
| Core arithmetic | Addition, subtraction, multiplication, division — each has at least one positive-integer test |
| Edge cases | Division by zero, negative operands, decimal operands, very large numbers, multiply-by-zero |
| Floating-point precision | `0.1 + 0.2` compared with `pytest.approx(0.3)` to avoid IEEE 754 false failures |
| Clear operation | Resetting a non-zero result to zero; clearing an already-zero state |
| CLI integration | Full input→output flows for all four operators; error surfacing for divide-by-zero and unknown operators; clear command via the CLI; sequential independent expressions |

## 3. What Was Not Tested (and Why)

| Area | Reason for exclusion |
|---|---|
| Performance / speed | Non-functional requirement outside the scope of a basic calculator assignment |
| UI rendering / styling | The application has no graphical interface |
| Concurrent / multi-user access | Single-process CLI with no shared state between sessions |
| Persistent storage | No state is written to disk; nothing to verify |
| Security / input sanitisation | Input is parsed as `float()` by Python, which safely rejects injections |

---

## 3. Lecture Concepts Applied

### 3.1 The Testing Pyramid

The testing pyramid prescribes that a healthy test suite has many fast, isolated unit tests at the base, fewer integration tests in the middle, and even fewer slow end-to-end tests at the top.

This suite mirrors that shape: **16 unit tests** sit at the base, testing individual `Calculator` methods in complete isolation with no I/O. **8 integration tests** form the middle layer, exercising the CLI-to-logic boundary by simulating real user sessions. There are no GUI or browser-level end-to-end tests, which is appropriate — the application has no graphical interface. The ratio (2:1 unit-to-integration) keeps the suite fast (total runtime < 0.1 s) and keeps failures easy to pinpoint, since a broken operation will first surface in the relevant unit test before appearing in integration output.

### 3.2 Black-Box vs White-Box Testing

**Unit tests** in this project are written as **white-box** tests. The author knows the internal implementation — for example, that `divide` raises `ValueError` with a specific message — and the tests assert on that exact internal contract (`pytest.raises(ValueError, match="Cannot divide by zero")`). The `clear` test also directly manipulates the internal `result` attribute to set up preconditions, which is only possible because the test has full visibility into the class internals.

**Integration tests** are written as **black-box** tests. They interact with the application exclusively through the public interface a real user would use: typed strings passed to `input()` and text printed to `stdout`. The tests assert only on the observable output (`"Result: 8" in output`) without knowing or caring how the calculator computed that value internally. This distinction matters because it mirrors how end-users experience the software.

### 3.3 Functional vs Non-Functional Testing

All tests in this suite are **functional** — they verify that the software does what it is specified to do (correct arithmetic, graceful error handling, accurate clear behaviour). Non-functional qualities such as performance, memory usage, security hardening, and accessibility are intentionally out of scope. For a command-line calculator operating on scalar numbers, these properties are either irrelevant or trivially satisfied by Python's own runtime guarantees. Documenting this boundary explicitly ensures the test suite remains focused and maintainable rather than bloated with tests that provide little signal.

### 3.4 Regression Testing

The existing test suite functions as a regression harness for all future changes. Any modification to `calculator.py` — a refactor, a new operation, a change to the division logic — will be immediately checked against all 24 tests when `pytest` is run. Because the tests are automated and require a single command, they can be integrated into a CI pipeline (e.g., GitHub Actions) so that every pull request is verified before merging. For example, if a future contributor accidentally changes `raise ValueError` to `return None` for division by zero, `test_divide_by_zero_raises` would catch it instantly, and `test_division_by_zero_shows_error` would provide a second confirmation at the integration level.

---

## 4. Test Results Summary

| Test Name | File | Type | Status |
|---|---|---|---|
| `test_add_positive_numbers` | test_calculator.py | Unit | PASS |
| `test_add_negative_numbers` | test_calculator.py | Unit | PASS |
| `test_add_mixed_sign_numbers` | test_calculator.py | Unit | PASS |
| `test_subtract_positive_numbers` | test_calculator.py | Unit | PASS |
| `test_subtract_resulting_in_negative` | test_calculator.py | Unit | PASS |
| `test_multiply_positive_numbers` | test_calculator.py | Unit | PASS |
| `test_multiply_by_zero` | test_calculator.py | Unit | PASS |
| `test_multiply_large_numbers` | test_calculator.py | Unit | PASS |
| `test_divide_positive_numbers` | test_calculator.py | Unit | PASS |
| `test_divide_returns_decimal` | test_calculator.py | Unit | PASS |
| `test_divide_by_zero_raises` | test_calculator.py | Unit | PASS |
| `test_divide_negative_dividend` | test_calculator.py | Unit | PASS |
| `test_add_decimal_numbers` | test_calculator.py | Unit | PASS |
| `test_multiply_decimal_numbers` | test_calculator.py | Unit | PASS |
| `test_clear_resets_result` | test_calculator.py | Unit | PASS |
| `test_clear_returns_zero_when_already_zero` | test_calculator.py | Unit | PASS |
| `test_addition_full_flow` | test_integration.py | Integration | PASS |
| `test_subtraction_full_flow` | test_integration.py | Integration | PASS |
| `test_multiplication_full_flow` | test_integration.py | Integration | PASS |
| `test_division_full_flow` | test_integration.py | Integration | PASS |
| `test_clear_after_calculation_resets_display` | test_integration.py | Integration | PASS |
| `test_division_by_zero_shows_error` | test_integration.py | Integration | PASS |
| `test_invalid_operator_shows_error` | test_integration.py | Integration | PASS |
| `test_sequential_operations_independent` | test_integration.py | Integration | PASS |

**Total: 24 tests — 24 passed, 0 failed.**
