import json
import os

class Storage:
    def __init__(self, filename):
        self.filepath = os.path.join(os.path.expanduser('~'), filename)

    def load_data(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f)
