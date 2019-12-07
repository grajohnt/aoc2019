from typing import Iterable
from typing import TextIO
from sys import stdin
from re import finditer
from re import search


def parse_input(io: TextIO) -> Iterable[str]:
    start, end = map(int, next(io).split('-'))
    return map(str, range(start, end + 1))


def is_increasing(password: str) -> bool:
    return ''.join(sorted(password)) == password


def has_double(password: str) -> bool:
    return search(r'(\d)\1', password) is not None


def has_exact_double(password: str) -> bool:
    return any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', password))


def part1(): 
    print(sum(1 for password in parse_input(stdin) if is_increasing(password) and has_double(password)))


def part2():
    print(sum(1 for password in parse_input(stdin) if is_increasing(password) and has_exact_double(password)))


