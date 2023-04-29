import re

l = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "?",
    "!",
]


def normal(text):
    i = 0
    j = len(text) - 1
    while i < len(text):
        if text[i] in l:
            break
        else:
            i += 1
    while j > 0:
        if text[j] in l or text[j] == ".":
            break
        else:
            j -= 1
    return re.sub("\s\s+", " ", text[i : j + 1])
