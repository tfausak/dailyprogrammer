"""http://redd.it/ywlvf

Today's easy challenge is to write a program that draws a number
in the terminal that looks like one of those old school seven segment
displays you find in alarm clocks and VCRs. For instance, if you
wanted to draw the number 5362, it would look somthing like:

    +--+  +--+  +--+  +--+
    |        |  |        |
    |        |  |        |
    +--+  +--+  +--+  +--+
       |     |  |  |  |
       |     |  |  |  |
    +--+  +--+  +--+  +--+

I've added some +'s to the joints to make it a bit more readable,
but that's optional.

Bonus: Write the program so that the numbers are scalable. In other
words, that example would have a scale of 2 (since every line is
two terminal characters long), but your program should also be able
to draw them in a scale of 3, 4, 5, etc.
"""
import sys


def seven_segment(mask):
    return ' {a} \n{f}{g}{b}\n{e}{d}{c}'.format(
        a='_' if mask & 0b0000001 else ' ',
        b='|' if mask & 0b0000010 else ' ',
        c='|' if mask & 0b0000100 else ' ',
        d='_' if mask & 0b0001000 else ' ',
        e='|' if mask & 0b0010000 else ' ',
        f='|' if mask & 0b0100000 else ' ',
        g='_' if mask & 0b1000000 else ' ',
    )


def render(number):
    masks = {
        0: 0b0111111,
        1: 0b0000110,
        2: 0b1011011,
        3: 0b1001111,
        4: 0b1100110,
        5: 0b1101101,
        6: 0b1111101,
        7: 0b0000111,
        8: 0b1111111,
        9: 0b1101111,
    }
    digits = [seven_segment(masks[int(digit)]).split('\n') for digit in number]
    return '\n'.join(''.join(digit + ' ' for digit in line)
        for line in zip(*digits))


def main(args):
    for arg in args:
        print render(arg)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
