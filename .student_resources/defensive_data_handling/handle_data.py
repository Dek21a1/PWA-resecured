import re
import html
import bcrypt

def check_PSWRD(password: str)  -> bytes:
    if not issubclass(type(password), str):
        raise TypeError("expected string")
    if not password.isalnum():
        raise ValueError("did not include all alphanumeric characters")
    if len(password) < 8:
        raise ValueError("too short, below 8 characters")
    if len(password) > 12:
        raise ValueError("too many characters, above 12")
    if not len(re.findall(r"[a-z]", password) + re.findall(r"[A-Z]", password)) >= 4:
        raise ValueError("incorrect amount of alpha characters")
    if not len(re.findall(r"[0-9]", password)) >= 3:
        raise ValueError("incorrect amount of numeric characters")
    return password.encode()