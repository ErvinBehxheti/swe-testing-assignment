# Quick-Calc

Quick-Calc is a lightweight command-line calculator that supports the four basic arithmetic operations — addition, subtraction, multiplication, and division — along with a clear function that resets the current result. The project is built with clean, testable Python and accompanied by a comprehensive test suite covering unit and integration scenarios.

## Setup Instructions

**Requirements:** Python 3.8 or higher.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/swe-testing-assignment.git
cd swe-testing-assignment

# (Optional) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install test dependencies
pip install pytest
```

## Running the Application

```bash
python main.py
```

Type an expression such as `5 + 3` and press Enter. Use `clear` (or `C`) to reset, and `quit` to exit.

## How to Run Tests

```bash
pytest
```

All tests are discovered automatically. For verbose output:

```bash
pytest -v
```

## Testing Framework Research

*(To be expanded in a later commit — section reserved for Pytest vs Unittest comparative analysis.)*
