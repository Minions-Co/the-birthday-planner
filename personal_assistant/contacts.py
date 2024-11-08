class ContactBook:
    def __init__(self):
        self.storage = Storage('contacts.json')
        self.contacts = self.load_contacts()

    def load_contacts(self):
        data = self.storage.load_data()
        return {name: Contact.from_dict(info) for name, info in data.items()}

    def save_contacts(self):
        data = {name: contact.to_dict() for name, contact in self.contacts.items()}
        self.storage.save_data(data)

    def add_contact(self, contact):
        contact.validate_email()
        for phone in contact.phones:
            contact.validate_phone(phone)
        self.contacts[contact.name] = contact
        self.save_contacts()
        print(f"Контакт '{contact.name}' додано.")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts.values():
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results

    def get_upcoming_birthdays(self, days):
        upcoming = []
        for contact in self.contacts.values():
            days_to_bday = contact.days_to_birthday()
            if days_to_bday is not None and days_to_bday <= days:
                upcoming.append(contact)
        return upcoming

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Контакт '{name}' видалено.")
        else:
            print(f"Контакт '{name}' не знайдено.")

    def edit_contact(self, name, field, value):
        if name in self.contacts:
            contact = self.contacts[name]
            if field == 'address':
                contact.address = value
            elif field == 'email':
                contact.email = value
                contact.validate_email()
            elif field == 'birthday':
                contact.birthday = value
            elif field == 'phones':
                phones = value.split(',')
                for phone in phones:
                    contact.validate_phone(phone.strip())
                contact.phones = [phone.strip() for phone in phones]
            else:
                print(f"Невідоме поле '{field}'.")
                return
            self.save_contacts()
            print(f"Контакт '{name}' оновлено.")
        else:
            print(f"Контакт '{name}' не знайдено.")
            