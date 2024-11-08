from difflib import get_close_matches

def parse_command(user_input):
    parts = user_input.strip().split(' ', 1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ''
    return command, args

class CommandHandler:
    def __init__(self, contact_book, note_book):
        self.contact_book = contact_book
        self.note_book = note_book
        self.commands = {
            'add_contact': self.add_contact,
            'search_contacts': self.search_contacts,
        }

    def handle(self, user_input):
        command, args = parse_command(user_input)
        if command in self.commands:
            self.commands[command](args)
        else:
            suggestion = self.suggest_command(command)
            print(f"Unknown command: {command}. Did you mean: {suggestion}?")

    def suggest_command(self, command):
        matches = get_close_matches(command, self.commands.keys(), n=1)
        return matches[0] if matches else 'no suggestion'

    def add_contact(self, args):
        print(f"Adding contact with details: {args}")

    def search_contacts(self, args):
        print(f"Searching contacts with query: {args}")
