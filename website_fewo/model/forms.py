import re


def validate_email(email):
    return re.match("(^[üäöÄÖÜa-zA-Z0-9_.+-]+@[üäöÄÖÜa-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
