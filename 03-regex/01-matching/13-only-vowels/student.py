import re
# Write your code here


def only_vowels(string):
    return re.fullmatch("[aeiou]*", string)
