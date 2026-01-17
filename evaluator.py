from typing import List

from _types import Token


def evaluate(expr: List[Token]) -> int:
    match expr:
        case [_, Token("OPERATOR", "+"), _]:
            left_num = expr[0].val
            right_num = expr[2].val
            return left_num + right_num
        case [_, Token("OPERATOR", "-"), _]:
            left_num = expr[0].val
            right_num = expr[2].val
            return left_num - right_num
        case [Token("NUMBER")]:
            left_num = expr[0].val
            return left_num
