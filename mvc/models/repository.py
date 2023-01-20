from database.database import Database
from events.event_manager import EventManager


class Repository:

    def __init__(self):
        self.events = EventManager()

    def get(self, _id: int):
        db = Database.get_instance()
        cursor = db.cursor
        cursor.execute("SELECT id, name, created_at FROM repositories WHERE id=?", (_id,))
        return cursor.fetchone()

    def index(self):
        db = Database.get_instance()
        cursor = db.cursor
        cursor.execute("SELECT id, name, created_at FROM repositories")
        return cursor.fetchall()

    def all(self):
        repositories = self.index()
        self.events.notify(event_type='github', key='repositories', data=repositories)

    def create(self, name_entry):
        def store():
            name = name_entry.get()
            db = Database.get_instance()
            db.cursor.execute("INSERT INTO repositories (name) VALUES (?)", (name,))
            db.conn.commit()
            self.all()
        return store

    def delete(self, _id):
        def _delete():
            db = Database.get_instance()
            db.cursor.execute("DELETE FROM repositories WHERE id = ?", (_id,))
            db.conn.commit()
            self.all()
        return _delete
