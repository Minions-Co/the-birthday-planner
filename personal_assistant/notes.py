from personal_assistant.storage import Storage


class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
    
    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
        }
    
    @staticmethod
    def from_dict(data):
        return Note(
            title=data['title'],
            content=data['content'],
            tags=data.get('tags', []),
        )
        
           
class NoteBook:
    def __init__(self):
        self.storage = Storage('notes.json')
        self.notes = self.load_notes()
    
    def load_notes(self):
        data = self.storage.load_data()
        return {title: Note.from_dict(info) for title, info in data.items()}
    
    def save_notes(self):
        data = {title: note.to_dict() for title, note in self.notes.items()}
        self.storage.save_data(data)
    
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
    
    