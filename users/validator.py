import re

def validate_email(email):
    is_email_regex = "^[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.]+"
    return re.match(is_email_regex, email)

def validate_password(password):
    is_password_regex = "[A-Za-z0-9'~!@#$%^&*()-=,.<>/?]{8,}"
    return re.match(is_password_regex, password)

def validate_first_name(first_name):
    is_first_name_regex = "^[A-Za-z]{1,}"
    return re.match(is_first_name_regex, first_name)

def validate_last_name(last_name):
    is_last_name_regex = "^[A-Za-z]{1,}"
    return re.match(is_last_name_regex, last_name)

def validate_dob(date_of_birth):
    is_dob_regex = "^(\d{4})-(\d{2})-(\d{2})"
    return re.match(is_dob_regex, date_of_birth)

