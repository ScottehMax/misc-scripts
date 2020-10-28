# coding: utf-8
"""Takes a set of GSC box names and converts them to the equivalent 
hexadecimal bytes."""

apos = {
    "'d": 0xd0,
    "'l": 0xd1,
    "'m": 0xd2,
    "'r": 0xd3,
    "'s": 0xd4,
    "'t": 0xd5,
    "'v": 0xd6,
    'Pk': 0xe1,
    'Mn': 0xe2
}

s = {
    "'d": 0xd0,
    "'l": 0xd1,
    "'m": 0xd2,
    "'r": 0xd3,
    "'s": 0xd4,
    "'t": 0xd5,
    "'v": 0xd6,
    " ": 0x7f,
    "A": 0x80,
    "B": 0x81,
    "C": 0x82,
    "D": 0x83,
    "E": 0x84,
    "F": 0x85,
    "G": 0x86,
    "H": 0x87,
    "I": 0x88,
    "J": 0x89,
    "K": 0x8a,
    "L": 0x8b,
    "M": 0x8c,
    "N": 0x8d,
    "O": 0x8e,
    "P": 0x8f,
    "Q": 0x90,
    "R": 0x91,
    "S": 0x92,
    "T": 0x93,
    "U": 0x94,
    "V": 0x95,
    "W": 0x96,
    "X": 0x97,
    "Y": 0x98,
    "Z": 0x99,

    "(": 0x9a,
    ")": 0x9b,
    ":": 0x9c,
    ";": 0x9d,
    "[": 0x9e,
    "]": 0x9f,

    "a": 0xa0,
    "b": 0xa1,
    "c": 0xa2,
    "d": 0xa3,
    "e": 0xa4,
    "f": 0xa5,
    "g": 0xa6,
    "h": 0xa7,
    "i": 0xa8,
    "j": 0xa9,
    "k": 0xaa,
    "l": 0xab,
    "m": 0xac,
    "n": 0xad,
    "o": 0xae,
    "p": 0xaf,
    "q": 0xb0,
    "r": 0xb1,
    "s": 0xb2,
    "t": 0xb3,
    "u": 0xb4,
    "v": 0xb5,
    "w": 0xb6,
    "x": 0xb7,
    "y": 0xb8,
    "z": 0xb9,
    "Pk": 0xe1,
    "Mn": 0xe2,
    "-": 0xe3,
    "?": 0xe6,
    "!": 0xe7,
    ".": 0xe8,
    "&": 0xe9,
    "é": 0xea,
    "♂": 0xef,
    "×": 0xf1,
    "/": 0xf3,
    ",": 0xf4,
    "♀": 0xf5,
    "0": 0xf6,
    "1": 0xf7,
    "2": 0xf8,
    "3": 0xf9,
    "4": 0xfa,
    "5": 0xfb,
    "6": 0xfc,
    "7": 0xfd,
    "8": 0xfe,
    "9": 0xff
}

def box_to_hex(box_str):
    res = ''
    while box_str:
        print(box_str)
        for c in list(apos.keys()) + list(s.keys()):
            if box_str.startswith(c):
                res += ' ' + hex(s[c])[2:]
                box_str = box_str[len(c):]
                break
    return res

final_res = ''
while True:
    inp = input("> ")
    if inp == '!quit':
        print(final_res)
        break
    final_res += box_to_hex(inp)