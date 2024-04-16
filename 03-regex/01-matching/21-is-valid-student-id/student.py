import re
# Write your code here


def is_valid_student_id(string):
    return re.fullmatch("[rsRS][0-9]{7}", string)
