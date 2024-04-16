import re
# Write your code here


def is_valid_email_address(string):
    return re.fullmatch("(.)+@(ucll.be|student.ucll.be)", string)
