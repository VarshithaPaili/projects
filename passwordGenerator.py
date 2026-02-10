import random
import string

def generate_strong_password(length):
    if length < 4:
        return "Password length should be at least 4"

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

        password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = lower + upper + digits + symbols

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)


length = int(input("Enter password length: "))
password = generate_strong_password(length)

print("Generated Strong Password:", password)
