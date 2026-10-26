def calculator():
    print("\n" + "=" * 35)
    print("       SMART CALCULATOR")
    print("=" * 35)

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                print("Error: Division by zero.")
                return
            result = a / b
        else:
            print("Invalid operator.")
            return

        print(f"\nResult: {result:g}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
