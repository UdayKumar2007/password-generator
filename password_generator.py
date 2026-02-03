import string
import secrets  # Better for security than 'random'

def generate_password(length, use_uppercase, use_digits, use_symbols):
    # Start with lowercase as the base
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Safety check: if length is 0 or negative
    if length <= 0:
        return "Error: Length must be greater than 0."

    # Use secrets.choice for cryptographic security
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Secure Password Generator")

    try:
        length = int(input("Enter password length: "))
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        
        print("-" * 30)
        print(f"Generated Password: {password}")
        print("-" * 30)
        
    except ValueError:
        print("Invalid input! Please enter a number for the length.")

if __name__ == "__main__":
    main()
