def criptChar(alphabet: list, charIndex: int, jumps: int) -> str:
    return str.lower(alphabet[((charIndex + jumps) - 26) if ((charIndex + jumps) > 25) else (charIndex + jumps)])

def getCharIndex(textChar: str, alphabet: list) -> int:
    for index, item in enumerate(alphabet):
        if str.lower(textChar) == str.lower(item):
            return int(index)

