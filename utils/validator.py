import re

def validate_email(email):
    EMAIL_REGEX = "^[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.]+"
    return re.match(EMAIL_REGEX, email)

def validate_password(password):
    PASSWORD_REGEX = "[A-Za-z0-9'~!@#$%^&*()-=,.<>/?]{8,}"
    return re.match(PASSWORD_REGEX, password)

def validate_first_name(first_name):
    FIRST_NAME_REGEX = "^[A-Za-z]{1,}"
    return re.match(FIRST_NAME_REGEX, first_name)

def validate_last_name(last_name):
    LAST_NAME_REGEX = "^[A-Za-z]{1,}"
    return re.match(LAST_NAME_REGEX, last_name)

def validate_date_of_birth(date_of_birth):
    DATE_OF_BIRTH_REGEX = "^(\d{4})-(\d{2})-(\d{2})"
    return re.match(DATE_OF_BIRTH_REGEX, date_of_birth)

