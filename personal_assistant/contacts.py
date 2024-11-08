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

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Контакт '{name}' видалено.")

    def edit_contact(self, name, field, value):
        if name in self.contacts:
            contact = self.contacts[name]
            setattr(contact, field, value)
            self.save_contacts()
            print(f"Контакт '{name}' оновлено.")
            