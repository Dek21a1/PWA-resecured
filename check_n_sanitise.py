import re
import html

def check_password(password: str) -> bytes:
    if not issubclass(type(password), str):
        raise TypeError("expected string")
    if not password.isalnum():
        raise ValueError("did not include all alphanumeric characters")