from secrets import randbelow

def generate_id(
        length: int,
        unique_chars: bool = True,
        allowed_chars: str = "RXETKAFYCJV234789"
        ) -> str:
    assert length <= len(allowed_chars)
    code = ""
    for i in range(length):
        c = ""
        while c in code:
            r = randbelow(len(allowed_chars))
            c = allowed_chars[r]
        code += c
    return code

print(generate_id(6))