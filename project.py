import pickle

class Note:
    def __init__(self,title,text):
        self.title = title
        self.text = text

def add_note():
    title = input("Введіть заголовок запису: ")
    text = input("Введіть текст запису: ")
    note = Note(title, text)
    return note

def save_notes(notes):
    with open("notes.pkl","wb") as f:
        pickle.dump(notes, f)

def load_notes():
    try:
        with open("notes.pkl","rb") as f:
            notes = pickle.load(f)
    except FileNotFoundError:
        notes = []
    return notes
def show_notes(notes):
    if len(notes) == 0:
        print("Записів не знайдено")
    else:
        for i, note in enumerate(notes):
            print(f"""{i + 1}-{note.title}
{note.text}""")
def edit_note(notes):
    show_notes(notes)
    index = int(input("Введіть номер запису для редагування: "))
    note = notes[index - 1]
    title = input("Введіть новий заголовок: ")
    text = input("Введіть новий текст: ")
    note.title = title
    note.text = text
def delete_note(notes):
    show_notes(notes)
    index = int(input("Введіть номер запису для редагування: "))
    del notes[index - 1]
def main():
    notes = load_notes()
    while True:
        choice = input(f"""Оберіть дію:
    1 - Додати запис
    2 - Редагувати запис
    3 - Видалити запис
    4 - Показати усі записи
    5 - Вихід
    : """)
        if choice == "1":
            note = add_note()
            notes.append(note)
            save_notes(notes)
        if choice == "2":
            edit_note(notes)
            save_notes(notes)
        if choice == "3":
            delete_note(notes)
            save_notes(notes)
        if choice == "4":
            show_notes(notes)
        if choice == "5":
            break
if __name__ == "__main__":
    main()
    
