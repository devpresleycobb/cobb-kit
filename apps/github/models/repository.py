from database import Database
from apps.github.views.view import View


class Repository:

    def __init__(self, id):
        self.id = id

    def get(self):
        db = Database.get_instance()
        cursor = db.cursor
        cursor.execute("SELECT id, name, created_at FROM repositories WHERE id=?", (self.id,))
        return cursor.fetchone()

    @staticmethod
    def all():
        db = Database.get_instance()
        cursor = db.cursor
        cursor.execute("SELECT id, name, created_at FROM repositories")
        return cursor.fetchall()

    @staticmethod
<<<<<<< Updated upstream:apps/github/repository.py
    def create(name) -> int:
        db = Database.get_instance()
        db.cursor.execute("INSERT INTO repositories (name) VALUES (?)", (name,))
        db.conn.commit()
        return db.cursor.lastrowid

    @staticmethod
    def delete(id) -> int:
        db = Database.get_instance()
        db.cursor.execute("DELETE FROM repositories WHERE id = ?", (id,))
        db.conn.commit()
        return id
=======
    def create(name_entry):
        @View.rerender
        def store() -> int:
            name = name_entry.get()
            db = Database.get_instance()
            db.cursor.execute("INSERT INTO repositories (name) VALUES (?)", (name,))
            db.conn.commit()
            return db.cursor.lastrowid
        return store
>>>>>>> Stashed changes:apps/github/models/repository.py

    @staticmethod
    def delete(_id):
        @View.rerender
        def _delete():
            db = Database.get_instance()
            db.cursor.execute("DELETE FROM repositories WHERE id = ?", (_id,))
            db.conn.commit()
            return _id
        return _delete
