import re


class InvalidPhoneError(Exception):
    pass


class Contact:
    def __init__(self, name, phone='', email=''):
        self.name = name
        self.phone = phone
        self.email = email

    def validate_phone(self):
        pattern = r'^\+?\d{9,15}$'
        if not re.match(pattern, self.phone):
            raise InvalidPhoneError("Invalid phone number.")
