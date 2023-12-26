import string
import random

# lists with ascii depending on type


print("-- Password Generator -- ")


def generate_password(all_options, password_length):
    create_password = ""
    for i in range(password_length):
        arr = random.choice(all_options)
        create_password += random.choice(arr)
    return create_password


def all_or_custom(password_length):
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    all_options = []
    if password_length == 0:
        all_options = [uppercase_letters, lowercase_letters, numbers, symbols]
        password_length = random.randint(10, 20)
    else:
        use_uppercase_letters = input("Do you want to use UPPERCASE LETTERS? (s/n): ").lower()
        if use_uppercase_letters == "s":
            all_options.append(uppercase_letters)
        use_lowercase_letters = input("Do you want to use LOWERCASE LETTERS? (s/n): ").lower()
        if use_lowercase_letters == "s":
            all_options.append(lowercase_letters)
        use_symbols = input("Do you want to use SYMBOLS? (s/n): ").lower()
        if use_symbols == "s":
            all_options.append(symbols)
        use_numbers = input("Do you want to use NUMBERS? (s/n): ").lower()
        if use_numbers == "s":
            all_options.append(numbers)
    return generate_password(all_options, password_length)


while True:
    password_length = int(input("Enter password length or random = 0: "))
    create_password = all_or_custom(password_length)
    print(f"Password: {create_password}")
    validate_exit = input("Press 'R' to generate another or 'Enter' to close...")
    if validate_exit.lower() != "r":
        break
