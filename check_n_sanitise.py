import re
import html
import bcrypt

def check_password(password: str) -> bytes:
    if not issubclass(type(password), str):
        raise TypeError("expected string")
    if not password.isalnum():
        raise ValueError("did not include all alphanumeric characters")
    if len(password) < 8:
        raise ValueError("Password length is below 8")
    if len(re.findall(r"[a-z]", password) + (r"[A-Z]", password)) <= 1:
        raise ValueError("not enough letters")
    if len(re.findall(r"[0-9]", password)) <= 1:
        raise ValueError("not enough numbers")
    return password.encode()