class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def search_contacts(self, query):
        results = []
        for contact in self.contacts.values():
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def edit_contact(self, name, field, value):
        if name in self.contacts:
            contact = self.contacts[name]
            setattr(contact, field, value)
            