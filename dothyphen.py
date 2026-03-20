'''
Interpreter for the language .dot-hyphen
By Proximath

Usage:

Code in the terminal
> echo "your code here" | python dothyphen.py

Read from file
> cat source-file.dot-hyphen | python dothyphen.py

Limit to n iterations
> echo "your code here" | python dothyphen.py --limit n

Debugging, print as integers, not ascii characters
> echo "your code here" | python dothyphen.py --debug
'''

from collections import defaultdict
import sys
from typing_extensions import Self
import argparse

sys.setrecursionlimit(100000)

arr: defaultdict[int, int] = defaultdict(lambda: 0)
argparser = argparse.ArgumentParser()
argparser.add_argument("-l", "--limit", type=int)
argparser.add_argument("-d", "--debug", action="store_true")

class Expr:
    left: Self | None
    right: Self | None
    num: int = -1

    def evaluate(self) -> int:
        if self.num != -1:
            return self.num
        elif self.left is not None and self.right is not None:
            x = self.left.evaluate()
            y = self.right.evaluate()
            arr[x] -= y
            return arr[x]
        else:
            raise RuntimeError(f"INTERNAL ERROR: Something's wrong")

def parse(code: str, index: int) -> tuple[Expr, int]:
    while index < len(code) and code[index] not in ['.', '-'] and not code[index].isdigit():
        index += 1
    if index >= len(code):
        print(f"SYNTAX ERROR: Expected expression at end of string")
        sys.exit(1)
    ret = Expr()
    if code[index].isdigit():
        ret.num = 0
        while index < len(code) and code[index].isdigit():
            ret.num = ret.num * 10 + int(code[index])
            index += 1
    elif code[index] == '.':
        ret.left, index = parse(code, index + 1)
        if index >= len(code):
            print(f"SYNTAX ERROR: Expected '-' at end of string")
            sys.exit(1)
        elif code[index] != '-':
            print(f"SYNTAX ERROR: Expected '-' at character #{index+1}")
            sys.exit(1)
        ret.right, index = parse(code, index + 1)
    else:
        print(f"SYNTAX ERROR: Unexpected {code[index]} at character #{index+1}")
        sys.exit(1)
    return ret, index

def main():
    args = argparser.parse_args()
    limit = args.limit
    debug_mode = args.debug
    code = sys.stdin.read()
    expr, index = parse(code, 0)
    while index < len(code) and code[index] not in ['.', '-'] and not code[index].isdigit():
        index += 1
    if index < len(code):
        print(f"SYNTAX ERROR: Unexpected {code[index]} at character #{index+1}, a valid program must contain only ONE expression")
        sys.exit(1)
    iteration = 0
    while limit is None or iteration < limit:
        res = expr.evaluate()
        if 0 <= res < 128 and not debug_mode:
            print(chr(res), end="")
        elif debug_mode:
            print(res, end="")
        iteration += 1

main()
