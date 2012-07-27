"""http://redd.it/x8rl8

Write a function that takes a number n as an argument and returns
(or outputs) every possible unique substrings (not counting "") of
the first n letters of the alphabet (in any order you like). For
example, substrings(5) could be:

    a
    ab
    abc
    abcd
    abcde
    b
    bc
    bcd
    bcde
    c
    cd
    cde
    d
    de
    e

BONUS 1: Find a way to quickly determine how many strings this
function returns for a given input. If the alphabet were 500 letters
long, how much possible substrings would it have?

BONUS 2: Modify your function to take a string as an argument. Make
sure all substrings in your output are still unique (i.e., there
are two "l" substrings in "hello", but you should output only one).
"""
import string
import sys


def substrings(n, alphabet=string.lowercase):
    result = []
    for start in range(n):
        for length in range(n - start):
            result.append(alphabet[start:start + length + 1])
    assert len(result) == (n * (n + 1)) / 2
    return result


def main(args):
    for arg in args:
        try:
            n = int(arg)
            result = substrings(n)
        except ValueError:
            letters = ''.join(sorted(set(arg)))
            result = substrings(len(letters), alphabet=letters)
        print n, len(result), result


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
