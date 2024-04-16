import re
# Write your code here


def ababa(string):
    return re.fullmatch(r'(.+)(.+)\1\2\1', string)
