class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        
class NoteBook:
    def __init__(self):
        self.notes = {}
    
    def add_note(self, note): # Функція додавання запису в примітки
        self.notes[note.title] = note
    
    def search_notes(self, query): # Функція пошуку
        results = []
        for note in self.notes.values():
            if query.lower() in note.content.lower() or query.lower() in note.title.lower():
                results.append(note)
        return results

    def search_by_tags(self, tags): # Функція пошуку за тегом
        results = []
        for note in self.notes.values():
            if set(tags).issubset(set(note.tags)):
                results.append(note)
        return results