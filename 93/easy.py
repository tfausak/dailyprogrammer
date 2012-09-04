"""http://redd.it/z3a4y

This challenge courtesy of user nagasgura

In this challenge, we read in a string from standard input and
output the translation to or from morse code on standard output.

When translating to Morse code, one space should be used to separate
morse code letters, and two spaces should be used to separate morse
code words. When translating to English, there should only be one
space in between words, and no spaces in between letters.

Here's a chart of the morse code symbols: [1]
http://www.w1wc.com/pdf_files/international_morse_code.pdf

Example input and output: 'sos' -> '... --- ...' '... --- ...' ->
'sos'
"""
import sys


TEXT_TO_MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}
MORSE_TO_TEXT = dict((morse, text) for text, morse in TEXT_TO_MORSE.items())


def text_to_morse(text):
    return '  '.join(
        ' '.join(
            TEXT_TO_MORSE[letter]
            for letter
            in word
            if letter in TEXT_TO_MORSE
        )
        for word
        in text.split()
    )


def morse_to_text(morse):
    return ' '.join(
        ''.join(
            MORSE_TO_TEXT[letter]
            for letter
            in word.split(' ')
            if letter in MORSE_TO_TEXT
        )
        for word
        in morse.split('  ')
    )



def main(args):
    print 'sos', text_to_morse('sos'), morse_to_text('... --- ...')
    print 'hello world', text_to_morse('hello world'), morse_to_text('.... . .-.. .-.. ---  .-- --- .-. .-.. -..')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
