import random
import string
import argparse

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    """Generates a random password based on user-defined criteria."""
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: You must select at least one character type."

    # Use SystemRandom for cryptographically secure random numbers
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password from the command line.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    args = parser.parse_args()

    # Pass the inverted boolean arguments to the generator
    password = generate_password(
        length=args.length,
        use_uppercase=not args.no_upper,
        use_numbers=not args.no_numbers,
        use_symbols=not args.no_symbols
    )

    print("\n🔒 Generated Password:")
    print("-" * 30)
    print(password)
    print("-" * 30 + "\n")

if __name__ == "__main__":
    main()
