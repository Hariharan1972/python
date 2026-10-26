import string


def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return levels[score]


def main():
    password = input("Enter a password to evaluate: ")
    print("Password Strength:", check_password(password))


if __name__ == "__main__":
    main()
