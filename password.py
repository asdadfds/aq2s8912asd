import random
import string

def generate_password(length):
    if length < 6 or length > 32:
        return "Довжина має бути від 6 до 32 символів!"

    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    while True:
        password = ''.join(random.sample(chars, length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()-_+=" for c in password)):
            return password

length = int(input("Довжина пароля: "))
print(generate_password(length))
