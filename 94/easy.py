"""http://redd.it/z6o4k

If you've ever seen Breaking Bad, you might have noticed how some
names in the opening credit sequence get highlights according to
symbols of elements in the periodic table. Given a string as input,
output every possible such modification with the element symbol
enclosed in brackets and capitalized. The elements can appear
anywhere in the string, but you must only highlight one element per
line, like this:

    $ ./highlight dailyprogrammer
    dailypr[O]grammer
    daily[P]rogrammer
    dail[Y]programmer
    da[I]lyprogrammer
    dailyprog[Ra]mmer
    daily[Pr]ogrammer
    dailyprogramm[Er]
    dailyprogr[Am]mer
"""
import re
import sys


PERIODIC_TABLE = ['h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na',
    'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr',
    'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr',
    'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd',
    'in', 'sn', 'sb', 'te', 'i', 'xe', 'cs', 'ba', 'lu', 'hf', 'ta', 'w', 're',
    'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr',
    'ra', 'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'uut',
    'uuq', 'uup', 'uuh', 'uus', 'uuo', 'la', 'ce', 'pr', 'nd', 'pm', 'sm',
    'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'ac', 'th', 'pa', 'u',
    'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no']


def break_bad(string):
    string = string.lower()
    result = []
    for symbol in PERIODIC_TABLE:
        pattern = '^(.*)({})(.*)$'.format(re.escape(symbol))
        for match in re.finditer(pattern, string):
            result.append('{}[{}]{}'.format(match.group(1),
                match.group(2).title(), match.group(3)))
    return result


def main(args):
    for arg in args:
        print break_bad(arg)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
