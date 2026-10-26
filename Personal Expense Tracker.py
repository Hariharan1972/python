import json
from pathlib import Path

FILE = Path("expenses.json")


def load_expenses():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved expenses.")
    return []


def save_expenses(expenses):
    FILE.write_text(
        json.dumps(expenses, indent=4),
        encoding="utf-8"
    )


def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ").strip()

            try:
                amount = float(input("Amount (₹): "))
                if not category or amount <= 0:
                    print("Enter a category and a positive amount.")
                    continue

                expenses.append({
                    "category": category,
                    "amount": amount
                })
                save_expenses(expenses)
                print("Expense saved successfully.")

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            for index, expense in enumerate(expenses, 1):
                print(
                    f"{index}. {expense['category']}: "
                    f"₹{expense['amount']:.2f}"
                )

            if not expenses:
                print("No expenses recorded.")

        elif choice == "3":
            total = sum(item["amount"] for item in expenses)
            print(f"Total Expenses: ₹{total:.2f}")

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
