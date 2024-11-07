import os
import json

class Storage:
    def __init__(self, filename):
        self.filepath = os.path.join(os.path.expanduser('~'), 'personal_assistant_data', filename)
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

       
            
