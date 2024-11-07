class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        
class NoteBook:
    def __init__(self):
        self.notes = {}
    
    def add_note(self, note):
        self.notes[note.title] = note