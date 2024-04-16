import re
# Write your code here


def two_or_more_abc(string):
    return re.fullmatch("(abc){2,}", string)
