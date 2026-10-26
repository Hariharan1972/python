import secrets
import string


def generate_password(length=16):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


if __name__ == "__main__":
    try:
        length = int(input("Enter password length (minimum 8): "))
        password = generate_password(length)

        print("\nGenerated Password:", password)

    except ValueError as error:
        print("Error:", error)
