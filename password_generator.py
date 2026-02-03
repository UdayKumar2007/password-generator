import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator")

    length = int(input("Enter password length: "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
