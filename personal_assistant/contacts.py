import re
from datetime import datetime
from dateutil.parser import parse as parse_date


class InvalidPhoneError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


class Contact:
    def __init__(self, name, address='', phones=None, email='', birthday=None):
        self.name = name
        self.address = address
        self.phones = phones if phones else []
        self.email = email
        self.birthday = birthday

    def validate_phone(self, phone):
        pattern = r'^\+?\d{9,15}$'
        if not re.match(pattern, phone):
            raise InvalidPhoneError(f"Invalid phone number: {phone}")

    def validate_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, self.email):
            raise InvalidEmailError(f"Invalid email address: {self.email}")

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            bday = datetime.strptime(self.birthday, '%Y-%m-%d')
            next_birthday = bday.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            return (next_birthday - today).days
        return None

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'phones': self.phones,
            'email': self.email,
            'birthday': self.birthday,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data['name'],
            address=data.get('address', ''),
            phones=data.get('phones', []),
            email=data.get('email', ''),
            birthday=data.get('birthday', None),
        )
