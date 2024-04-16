import re


def main():
    username = input("Username: ")
    password = input("Password: ")

    result = bool(
        re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}", password))

    if result:
        print(f"Succesfully registered with username: {username}!")
    else:
        print("""
Password must contain:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
              """)


main()
