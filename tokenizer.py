from typing import List

from _types import Token


def is_numeric(char: str) -> bool:
    match char:
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            return True

    return False


def is_blank(char: str) -> bool:
    if char == " ":
        return True
    elif char == "\t":
        return True

    return False


def tokenize(text: str) -> List[Token] | None:
    tokens = []

    curr_pos = 0
    while curr_pos < (len(text)):
        char = text[curr_pos]

        if is_blank(char):
            curr_pos += 1
            continue
        elif char == "+" or char == "-":
            tokens.append(Token("OPERATOR", char))
            curr_pos += 1
        elif is_numeric(char):
            number = ""
            while curr_pos < len(text) and is_numeric(char):
                char = text[curr_pos]
                number += char
                curr_pos += 1

            tokens.append(Token("NUMBER", int(number)))
        else:
            raise RuntimeError(
                f"[ERROR] Not able to parse token: '{char}' at position {curr_pos}"
            )

    print(f"[DEBUG] Tokens: {tokens}")
    return tokens
