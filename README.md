# Quick-Calc

Quick-Calc is a lightweight command-line calculator that supports the four basic arithmetic operations — addition, subtraction, multiplication, and division — along with a clear function that resets the current result. The project is built with clean, testable Python and accompanied by a comprehensive test suite covering both unit and integration scenarios.

## Setup Instructions

**Requirements:** Python 3.8 or higher.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/swe-testing-assignment.git
cd swe-testing-assignment

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install test dependencies
pip install pytest
```

## Running the Application

```bash
python3 main.py
```

Type an expression such as `5 + 3` and press Enter. Use `clear` (or `C`) to reset the result to zero, and `quit` to exit.

**Supported operators:** `+`  `-`  `*`  `/`

## How to Run Tests

```bash
python3 -m pytest -v
```

This discovers and runs all 24 tests (16 unit, 8 integration) automatically. No flags or configuration files are required beyond pytest being installed.

---

## Testing Framework Research

### Pytest vs Unittest — A Comparative Analysis

Python ships with two mainstream testing solutions: the built-in `unittest` module and the third-party `pytest` library. `unittest` follows the xUnit pattern popularised by JUnit. Tests are written as classes that inherit from `unittest.TestCase`, and assertions are made through dedicated methods such as `assertEqual`, `assertRaises`, and `assertAlmostEqual`. Because it is part of the standard library, `unittest` requires zero installation and is familiar to developers coming from Java or C# backgrounds. Its main drawbacks are verbosity and ceremony: even a trivial test requires a class definition, a method prefixed with `test_`, and the use of `self`, which adds friction when writing or reading large test suites.

`pytest` takes a radically different approach. Tests are plain functions — no class inheritance, no `self`, no special assertion methods. The standard Python `assert` statement is sufficient; pytest rewrites it at collection time to produce detailed failure messages that show the exact values that differed. The fixture system (the `@pytest.fixture` decorator) provides dependency injection for shared state, replacing the rigid `setUp`/`tearDown` lifecycle of `unittest` with a composable, reusable alternative. `pytest` also has a rich plugin ecosystem — coverage reporting, parallel execution, HTML reports — available via simple pip installs. The main trade-off is that it is an external dependency, which may matter in locked-down corporate or embedded environments.

For this project, **pytest** was chosen for three reasons. First, the plain-function style keeps the test file readable at a glance, which directly supports the assignment's goal of demonstrating clear, professional testing. Second, `pytest.approx` handles floating-point comparisons elegantly — a genuine need given that the calculator works with decimal numbers. Third, the fixture system allows a fresh `Calculator` instance to be injected into every unit test with a single `@pytest.fixture` decorator, avoiding repetitive setup code without sacrificing test isolation.
