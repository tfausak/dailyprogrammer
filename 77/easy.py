"""http://redd.it/wn3ld

Morse code, as we are all aware, consists of dots and dashes. Lets
define a "Morse code sequence" as simply a series of dots and dashes
(and nothing else). So ".--.-.--" would be a morse code sequence,
for instance.

Dashes obviously take longer to transmit, that's what makes them
dashes. Lets say that a dot takes 1 unit of time to transmit, and
a dash takes 2 units of time. Then we can say that the "size" of a
certain morse code sequence is the sum of the time it takes to
transmit the dots and dashes. So, for instance "..-." would have a
size of 5 (since there's three dots taking three units of time and
one dash taking two units of time, for a total of 5). The sequence
"-.-" would also have a size of 5.

In fact, if you list all the the possible Morse code sequences of
size 5, you get:

.....  ...-  ..-.  .-..  -...  .--  -.-  --.

A total of 8 different sequences.

Your task is to write a function called Morse(X) which generates
all morse code sequences of size X and returns them as an array of
strings (so Morse(5) should return the 8 strings I just mentioned,
in some order).

Use your function to generate and print out all sequences of size
10.

* * *

Bonus: Try and write your code so that it can generate Morse(35)
(or even Morse(36) or higher, but that takes a significant amount
of memory) in a "reasonable" amount of time. "Reasonable" obviously
depend on what computer and programming language you are using, but
a good rule of thumb should be that it should finish in less than
a minute.
"""
import itertools
import sys


def morse(length):
    """Generate all Morse code sequences of the given length.

    A dot (".") has a length of 1 and a dash ("-") has a length of 2.
    """
    result = set()
    for dots in range(length + 1):
        for dashes in range((length / 2) + 1):
            if (dots * 1) + (dashes * 2) == length:
                result |= set(''.join(character for character in permutation)
                    for permutation in itertools.permutations(
                        (dots * '.') + (dashes * '-')))
    return result


def main(args):
    for arg in args:
        try:
            length = int(arg)
        except ValueError:
            continue
        print length, sorted(morse(length))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
