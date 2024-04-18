import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNUmOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str):
    try:
        float(string)
        valid = True
    except:
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0