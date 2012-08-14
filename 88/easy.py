# -*- coding: utf-8 -*-
"""http://redd.it/y5sox

The easy challenge today is to implement the famous Vigenère cipher.
The Wikipedia article explains well how it works, but here's a short
description anyway:

You take a message that you want to encrypt, for instance "THECAKEISALIE"
(lets assume that all characters are upper-case and there are no
spaces in the messages, for the sake of simplicity), and a key you
want to encrypt it with, for instance "GLADOS". You then write the
message with the key repeated over it, like this:

    GLADOSGLADOSG
    THECAKEISALIE

The key is repeated as often as is needed to cover the entire message.

Now, one by one, each letter of the key is "added" to the letter
of the clear-text to produce the cipher-text. That is, if A = 0, B
= 1, C = 2, etc, then E + G = K (because E = 4 and G = 6, and 4 +
6 = 10, and K = 10). If the sum is larger than 25 (i.e. larger than
Z), it starts from the beginning, so S + K = C (i.e. 18 + 10 = 28,
and 28 - 26 is equal to 2, which is C).

For a full chart of how characters combine to form new characters,
see here

The cipher text then becomes:

    GLADOSGLADOSG
    THECAKEISALIE
    -------------
    ZSEFOCKTSDZAK

Write funtions to both encrypt and decrypt messages given the right
key.

As an optional bonus, decrypt the following message, which has been
encrypted with a word that I've used in this post:

    HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLN
    BASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABB
    AISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISY
    MAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR

As an additional challenge, attempt to pronounce "Vigenère" properly.
I think it's like "Viche-en-ere", but I'm not entirely sure.
"""
import sys


def vigenere(key, message, flag=False):
    cipher = ''
    for index, character in enumerate(message):
        x = ord(character)
        x -= 65
        character = key[index % len(key)]
        y = ord(character)
        y -= 65
        if flag:
            x -= y
        else:
            x += y
        x %= 26
        x += 65
        character = chr(x)
        cipher += character
    return cipher


def main(args):
    print vigenere('GLADOS', 'THECAKEISALIE')
    keys = [
        'a', 'added', 'additional', 'all', 'an', 'and', 'anyway',
        'are', 'article', 'as', 'assume', 'attempt', 'b', 'because',
        'becomes', 'been', 'beginning', 'bonus', 'both', 'but',
        'by', 'c', 'challenge', 'characters', 'chart', 'cipher',
        'ciphertext', 'cleartext', 'combine', 'cover', 'decrypt',
        'description', 'e', 'each', 'easy', 'encrypt', 'encrypted',
        'entire', 'entirely', 'equal', 'etc', 'explains', 'famous',
        'following', 'for', 'form', 'from', 'full', 'funtions',
        'g', 'given', 'glados', 'gladosgladosg', 'has', 'here',
        'heres', 'how', 'i', 'ie', 'if', 'im', 'implement', 'in',
        'instance', 'is', 'it', 'its', 'ive', 'k', 'key', 'larger',
        'lets', 'letter', 'like', 'message', 'messages', 'needed',
        'new', 'no', 'not', 'now', 'of', 'often', 'one', 'optional',
        'over', 'post', 'produce', 'pronounce', 'properly', 'repeated',
        'right', 's', 'sake', 'see', 'short', 'simplicity', 'so',
        'spaces', 'starts', 'sum', 'sure', 'take', 'text', 'than',
        'that', 'the', 'thecakeisalie', 'then', 'there', 'think',
        'this', 'to', 'today', 'uppercase', 'used', 'vicheenere',
        'vigenere', 'want', 'well', 'which', 'wikipedia', 'with',
        'word', 'works', 'write', 'you', 'z',
    ]
    for key in keys:
        print key, vigenere(key.upper(), 'HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLNBASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABBAISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISYMAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR', flag=True).lower()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
