"""Main functions"""
import re

def is_palindrome(string: str) -> bool:
    td = string.lower()
    a1 = re.sub("[.,! s?@:;]", "", td)
    string_invertida = a1[::-1]
    if a1 == string_invertida:
        return True
    else:
        return False

