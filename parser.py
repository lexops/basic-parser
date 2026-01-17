from typing import List
from evaluator import evaluate

from _types import Token


def parse(expr: List[Token]) -> None:
    match expr:
        case [Token("NUMBER"), Token("OPERATOR"), Token("NUMBER")]:
            print("[DEBUG] Valid expression!")
            print(evaluate(expr))
        case [Token("NUMBER")]:
            print("[DEBUG] Valid expression!")
            print(evaluate(expr))
        case _:
            raise RuntimeError(f"[ERROR] Invalid expression {expr}.")
