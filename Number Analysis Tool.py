def analyze_numbers(numbers):
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "even_count": sum(n % 2 == 0 for n in numbers),
        "odd_count": sum(n % 2 != 0 for n in numbers)
    }


def main():
    print("\n=== NUMBER ANALYSIS TOOL ===")

    try:
        values = input("Enter numbers separated by spaces: ")
        numbers = [float(value) for value in values.split()]

        if not numbers:
            print("Please enter at least one number.")
            return

        report = analyze_numbers(numbers)

        print("\n--- ANALYSIS REPORT ---")
        for key, value in report.items():
            print(f"{key.replace('_', ' ').title()}: {value:g}")

    except ValueError:
        print("Please enter valid numbers only.")


if __name__ == "__main__":
    main()
