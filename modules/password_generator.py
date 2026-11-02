import secrets
import string

def generate_password(length=12):
    if not 8 <= length <= 63:
        raise ValueError("Password harus 8-63 karakter.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%&*"

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    chars = lowercase + uppercase + digits + symbols

    password.extend(
        secrets.choice(chars)
        for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
