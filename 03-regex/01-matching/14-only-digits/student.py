import re
# Write your code here


def only_digits(string):
    return re.fullmatch("[0-9]*", string)
