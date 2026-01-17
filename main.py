import sys

from tokenizer import tokenize
from parser import parse

while True:
    print(">>> ", end="")
    text = input()

    try:
        tokens = tokenize(text)
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        parse(tokens)
    except Exception as e:
        print(e)
        sys.exit(1)
