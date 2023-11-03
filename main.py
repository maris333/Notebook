import sqlite3
from datetime import datetime


class Notebook:
    def __init__(self):
        self.conn = sqlite3.connect('notebook.db')
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Notes(name TEXT UNIQUE, content TEXT, created_at TEXT);"
        self.conn.execute(query)

    def add_note(self, name, content):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO Notes(name, content, created_at) VALUES(?, ?, ?)"
        self.conn.execute(query, (name, content, created_at))
        self.conn.commit()

    def delete_note(self, name):
        query = "DELETE FROM Notes WHERE name = ?"
        self.conn.execute(query, (name,))
        self.conn.commit()

    def display_notes(self):
        query = "SELECT name, content, created_at FROM Notes"
        cursor = self.conn.execute(query)
        notes = cursor.fetchall()
        for note in notes:
            print("Name:", note[0])
            print("Content:", note[1])
            print("Created at:", note[2])
            print("")

    def __del__(self):
        self.conn.close()


notebook = Notebook()

while True:
    print("1. Add a note")
    print("2. Delete a note")
    print("3. Display all notes")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter note name: ")
        content = input("Enter note content: ")
        notebook.add_note(name, content)
        print("Note added successfully.")

    elif choice == "2":
        name = input("Enter note name to delete: ")
        notebook.delete_note(name)
        print("Note deleted successfully.")

    elif choice == "3":
        print("All notes:")
        notebook.display_notes()

    elif choice == "4":
        break

    print("")

