from difflib import get_close_matches

class CommandHandler:
   

    def handle(self, command, args): # Функція аналізу введеного тескту для системи підказок 
        if command in self.commands:
            self.commands[command](args)
        else:
            suggestion = self.suggest_command(command)
            print(f"Невідома команда: {command}. Можливо, ви мали на увазі: {suggestion}?")
    
    def suggest_command(self, command):
        matches = get_close_matches(command, self.commands.keys(), n=1, cutoff=0.6)
        return matches[0] if matches else 'невідома команда'