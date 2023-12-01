def cipher(text: str, offset: int) -> str:
    """
    >>> cipher("abc l XYZ.", 1)
    'bcd m YZA.'
    >>> cipher('bcd m YZA.', -1) # negative offset means decipher
    'abc l XYZ.'
    """
    return "".join(chr((ord(l) - ord("a" if l.islower() else "A") + offset) % 26 + ord("a" if l.islower() else "A")) if l.isalpha() else l for l in text)
