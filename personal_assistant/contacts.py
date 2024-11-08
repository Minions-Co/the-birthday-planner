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
    