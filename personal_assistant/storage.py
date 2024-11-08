import json
import os

class Storage:
    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.join(os.path.expanduser('~'), 'personal_assistant_data', self.filename)
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def load_data(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
