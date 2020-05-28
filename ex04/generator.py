import os
import sys
from base64 import b64encode


def get_random_int():
    return int.from_bytes(os.urandom(4), sys.byteorder)


def generator(text, sep=" ", option=None):
    words_list = text.split(sep)
    if type(text) == str:
        if option is None:
            return words_list
        elif option == "shuffle":
            return sorted(words_list, key=lambda x: get_random_int())
        elif option == "ordered":
            return sorted(words_list)
        return "ERROR"
    return "ERROR"
