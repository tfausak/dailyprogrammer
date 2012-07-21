"""http://redd.it/wvcv9

Write a program that converts a "plain" .pgm file passed from stdin
to an ASCII representation easily viewable in a terminal. If you're
too lazy to read through the specification, the format should be
simple enough to reverse-engineer from an example file:

    P2
    # feep.pgm
    24 7
    15
    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    0  3  3  3  3  0  0  7  7  7  7  0  0 11 11 11 11  0  0 15 15 15 15  0
    0  3  0  0  0  0  0  7  0  0  0  0  0 11  0  0  0  0  0 15  0  0 15  0
    0  3  3  3  0  0  0  7  7  7  0  0  0 11 11 11  0  0  0 15 15 15 15  0
    0  3  0  0  0  0  0  7  0  0  0  0  0 11  0  0  0  0  0 15  0  0  0  0
    0  3  0  0  0  0  0  7  7  7  7  0  0 11 11 11 11  0  0 15  0  0  0  0
    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0

-   The top line, P2, is there to identify the file as a plain .pgm file.
-   Lines with a # in front of them are comments, and should be ignored.
-   The first two numbers in the file are the width and height.
-   The third number, 15 here, is the maximum grayscale value in
    the image: here, this means 15 is full white, and lower numbers are
    darker, 0 being pure black.
-   Thereafter, a (width x height) grid specifying the image itself follows.

Your program should use ASCII symbols to represent different grayscale
values. Assuming the text is black on a white background, you could
use a gradient like this one:

    " .:;+=%$#"

Converted, the example image would look something like this:

    ....  ;;;;  ====  ####
    .     ;     =     #  #
    ...   ;;;   ===   ####
    .     ;     =     #
    .     ;;;;  ====  #
"""
import re
import sys


def parse_pgm(pgm):
    if pgm[:2] != 'P2':
        raise ValueError('Unknown image format')
    pgm = re.sub(r'#.*$', '', pgm, flags=re.MULTILINE)

    tokens = pgm.split()
    width = int(tokens[1])
    height = int(tokens[2])
    maximum = int(tokens[3])
    pixels = tokens[4:]

    image = [
        [
            float(pixels[x + (y * width)]) / maximum
            for x in range(width)
        ]
        for y in range(height)
    ]

    gradient = u'\u2588\u2593\u2592\u2591 '
    scale = len(gradient) - 1
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            row[x] = gradient[int(round(pixel * scale))]
        image[y] = ''.join(row)
    print '\n'.join(image)


def main(args):
    parse_pgm(sys.stdin.read())


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
