# 158689833

import sys
import string


DIGITS = set(string.digits)
BASE_10 = 10


def decode_string(s: str) -> list[str]:
    stack: list[tuple[list[str], int]] = []
    current_str: list[str] = []
    current_num: int = 0

    for ch in s:
        if ch in DIGITS:
            current_num = current_num * BASE_10 + int(ch)
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

    return current_str


def main() -> None:
    s = sys.stdin.readline().strip()
    decoded_list = decode_string(s)
    print(*decoded_list, sep='')


if __name__ == '__main__':
    main()
