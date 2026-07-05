import random
import re

# Password Generator
def character_caps():
    return chr(random.randint(65, 90))

def character_small():
    return chr(random.randint(97, 122))

def numbers():
    return str(random.randint(0, 9))

def symbol():
    return random.choice(["@", "#", "$", "&", "!", "%"])

def generate_password():
    length = int(input("Enter password length : "))

    if length < 4:
        print("Password length must be at least 4!")
        return

    password = [
        character_caps(),
        character_small(),
        numbers(),
        symbol()
    ]

    for _ in range(length - 4):
        password.append(random.choice([
            character_caps,
            character_small,
            numbers,
            symbol
        ])())

    random.shuffle(password)

    print("\nGenerated Password:")
    print("".join(password))

# Password validator stepwise
def validate_stepwise():
    password = input("Enter password : ")

    if len(password) < 8:
        print("Password must be at least 8 characters")
    elif not re.search(r"[A-Z]", password):
        print("Must contain an uppercase letter")
    elif not re.search(r"[a-z]", password):
        print("Must contain a lowercase letter")
    elif not re.search(r"\d", password):
        print("Must contain a digit")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Must contain a special character")
    else:
        print("Password is valid")

# Password validator regex
def validate_regex():
    password = input("Enter password : ")

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'

    if re.match(pattern, password):
        print("Password is valid")
    else:
        print("Password does not meet complexity requirements")

def password_strength():
    password = input("Enter password : ")
    score = 0

    if len(password) >= 8:
        print("Length: Pass")
        score += 1
    else:
        print("Length : Fail")
    if re.search(r"[A-Z]", password):
        print("Uppercase : Pass")
        score += 1
    else:
        print("Uppercase: Fail")
    if re.search(r"[a-z]", password):
        print("Lowercase : Pass")
        score += 1
    else:
        print("Lowercase: Fail")
    if re.search(r"\d", password):
        print("Digit : Pass")
        score += 1
    else:
        print("Digit: Fail")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Special Character : Pass")
        score += 1
    else:
        print("Special Character : Fail")

    print()
    if score == 5:
        print("Password Strength : Strong")
    elif score >= 3:
        print("Password Strength : Medium")
    else:
        print("Password Strength : Weak")


while True:
    print("PASSWORD UTILITY".center(100))
    print("\n1. Generate Password")
    print("2. Validate Password (Step-by-Step)")
    print("3. Validate Password (Regex)")
    print("4. Password Strength ")
    print("5. Exit")

    choice = int(input("\nEnter choice : "))

    match choice:
        case 1 :
            generate_password()
        case 2 :
            validate_stepwise()
        case 3 :
            validate_regex()
        case 4 :
            password_strength()
        case 5 :
            break