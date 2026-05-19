from calculator import Calculator


def run():
    calc = Calculator()
    print("Quick-Calc — type 'help' for usage, 'quit' to exit")

    while True:
        user_input = input("\nEnter expression (e.g. 5 + 3) or command: ").strip()

        if user_input.lower() in ("quit", "exit"):
            break

        if user_input.lower() in ("clear", "c"):
            print(f"Result: {calc.clear()}")
            continue

        if user_input.lower() == "help":
            print("  Supported operators: + - * /")
            print("  Commands: clear (C), quit")
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Error: expected format '<number> <operator> <number>'")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Error: invalid number")
            continue

        try:
            if op == "+":
                calc.result = calc.add(a, b)
            elif op == "-":
                calc.result = calc.subtract(a, b)
            elif op == "*":
                calc.result = calc.multiply(a, b)
            elif op == "/":
                calc.result = calc.divide(a, b)
            else:
                print(f"Error: unknown operator '{op}'")
                continue

            display = int(calc.result) if calc.result == int(calc.result) else calc.result
            print(f"Result: {display}")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run()
