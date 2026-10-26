def run_quiz():
    questions = [
        {
            "question": "Which language is used for Python development?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
            "answer": "A"
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["A. String", "B. Boolean", "C. List", "D. Float"],
            "answer": "B"
        },
        {
            "question": "Which keyword defines a function?",
            "options": ["A. class", "B. loop", "C. def", "D. return"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n=== PYTHON KNOWLEDGE QUIZ ===")

    for number, item in enumerate(questions, 1):
        print(f"\n{number}. {item['question']}")

        for option in item["options"]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"\nFinal Score: {score}/{len(questions)}")
    print(f"Percentage: {score / len(questions) * 100:.1f}%")


if __name__ == "__main__":
    run_quiz()
