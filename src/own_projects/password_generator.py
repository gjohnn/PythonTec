import string
import random
#lists with ascii depending on type
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)
all_options = []

print("-- Password Generator -- ")

password_length = int(input("Enter password length: "))
#validate what to include in password
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
create_password = ""

#choose random character and add it to password i times
for i in range(password_length):
    arr = random.choice(all_options)
    create_password += random.choice(arr)

print(f"Password: {create_password}")
