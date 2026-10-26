import json
from pathlib import Path
from datetime import datetime


class FinanceManager:
    def __init__(self, filename="finance_data.json"):
        self.filename = Path(filename)
        self.transactions = self.load_data()

    def load_data(self):
        if self.filename.exists():
            try:
                with self.filename.open("r", encoding="utf-8") as file:
                    data = json.load(file)

                if isinstance(data, list):
                    return data

                print("Warning: Invalid data format.")
            except (json.JSONDecodeError, OSError):
                print("Warning: Could not load saved data.")

        return []

    def save_data(self):
        try:
            with self.filename.open("w", encoding="utf-8") as file:
                json.dump(self.transactions, file, indent=4)
            return True
        except OSError:
            print("Error: Could not save transaction data.")
            return False

    def add_transaction(self, transaction_type, amount, category, note):
        transaction = {
            "id": len(self.transactions) + 1,
            "type": transaction_type,
            "amount": round(amount, 2),
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.transactions.append(transaction)

        if self.save_data():
            print("\nTransaction added successfully!")
        else:
            self.transactions.pop()
            print("Transaction was not saved.")

    def show_transactions(self):
        print("\n" + "=" * 75)
        print("TRANSACTION HISTORY")
        print("=" * 75)

        if not self.transactions:
            print("No transactions available.")
            return

        for transaction in self.transactions:
            print(
                f"ID: {transaction['id']} | "
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f} | "
                f"{transaction['category']} | "
                f"{transaction['note']}"
            )

    def show_summary(self):
        income = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Income"
        )

        expenses = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Expense"
        )

        print("\n" + "=" * 40)
        print("       FINANCIAL SUMMARY")
        print("=" * 40)
        print(f"Total Income   : ₹{income:.2f}")
        print(f"Total Expenses : ₹{expenses:.2f}")
        print(f"Current Balance: ₹{income - expenses:.2f}")
        print("=" * 40)

    def search_transactions(self, keyword):
        keyword = keyword.lower()

        results = [
            t for t in self.transactions
            if keyword in t["category"].lower()
            or keyword in t["note"].lower()
        ]

        if not results:
            print("No matching transactions found.")
            return

        print("\nSEARCH RESULTS")

        for transaction in results:
            print(
                f"ID: {transaction['id']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f} | "
                f"{transaction['category']} | "
                f"{transaction['note']}"
            )


def get_amount():
    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return None

        return amount

    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    manager = FinanceManager()

    while True:
        print("\n" + "=" * 45)
        print("       PERSONAL FINANCE MANAGER")
        print("=" * 45)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Financial Summary")
        print("5. Search Transactions")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice in ("1", "2"):
            amount = get_amount()

            if amount is None:
                continue

            category = input("Enter category: ").strip()
            note = input("Enter note: ").strip()

            if not category:
                print("Category cannot be empty.")
                continue

            transaction_type = (
                "Income" if choice == "1" else "Expense"
            )

            manager.add_transaction(
                transaction_type,
                amount,
                category,
                note
            )

        elif choice == "3":
            manager.show_transactions()

        elif choice == "4":
            manager.show_summary()

        elif choice == "5":
            keyword = input(
                "Enter category or keyword to search: "
            ).strip()

            if keyword:
                manager.search_transactions(keyword)
            else:
                print("Please enter a search keyword.")

        elif choice == "6":
            print("\nThank you for using Finance Manager!")
            print("Your data is stored locally.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()

