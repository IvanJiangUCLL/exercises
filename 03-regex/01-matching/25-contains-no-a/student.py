import re
# Write your code here


def contains_no_a(string):
    return re.fullmatch("[^a]*", string)
