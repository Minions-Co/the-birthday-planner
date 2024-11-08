class Contact:
    class InvalidEmailError(Exception):
    pass


class Contact:
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

    def validate_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, self.email):
            raise InvalidEmailError("Invalid email address.")

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data['name'],
            phone=data.get('phone', ''),
            email=data.get('email', ''),
        )
