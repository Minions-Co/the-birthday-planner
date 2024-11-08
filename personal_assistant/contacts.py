from personal_assistant.storage import Storage

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
        