import re

pw_regex = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
pw_validator = re.compile(pw_regex)
password = ""

while not pw_validator.fullmatch(password):
    password = input('give me a password validate: ')
