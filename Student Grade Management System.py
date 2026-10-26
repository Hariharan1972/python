def calculate_grade(marks):
    if not 0 <= marks <= 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    print("\n=== STUDENT GRADE MANAGER ===")

    name = input("Student Name: ").strip()

    try:
        marks = float(input("Enter marks (0-100): "))

        if not name or not 0 <= marks <= 100:
            print("Enter a valid name and marks.")
            return

        print("\n--- STUDENT REPORT ---")
        print("Name:", name)
        print(f"Marks: {marks:g}/100")
        print("Grade:", calculate_grade(marks))

    except ValueError:
        print("Please enter valid numeric marks.")


if __name__ == "__main__":
    main()
