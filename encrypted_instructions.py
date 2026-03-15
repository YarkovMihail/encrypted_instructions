# 158603199

import sys
from typing import List


def decode_string(s: str) -> str:
    stack: List[tuple[List[str], int]] = []
    current_str: List[str] = []
    current_num: int = 0

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            stack.append((current_str, current_num))
            current_str = []
            current_num = 0
        elif ch == ']':
            prev_str, num = stack.pop()
            repeated = ''.join(current_str) * num
            current_str = prev_str + [repeated]
        else:
            current_str.append(ch)

    return ''.join(current_str)


def main() -> None:
    s = sys.stdin.readline().strip()
    print(decode_string(s))


if __name__ == "__main__":
    main()
