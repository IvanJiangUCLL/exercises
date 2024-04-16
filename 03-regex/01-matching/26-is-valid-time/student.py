import re
# Write your code here


def is_valid_time(string):
    return re.fullmatch(r"([01][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(.\d{3})?", string)
