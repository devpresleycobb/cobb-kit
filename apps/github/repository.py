from database import Database


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
    def create(name) -> int:
        db = Database.get_instance()
        db.cursor.execute("INSERT INTO repositories (name) VALUES (?)", (name,))
        db.conn.commit()
        return db.cursor.lastrowid

    @staticmethod
    def update(id, data) -> None:
        db = Database.get_instance()
        db.cursor.execute("UPDATE repositories SET name = ? WHERE id = ?", (data['name'], id))
        db.conn.commit()

    @staticmethod
    def delete(id) -> int:
        db = Database.get_instance()
        db.cursor.execute("DELETE FROM repositories WHERE id = ?", (id,))
        db.conn.commit()
        return id

    @staticmethod
    def get_id_from_name(name):
        db = Database.get_instance()
        cursor = db.cursor
        cursor.execute("SELECT id FROM repositories WHERE name=?", (name,))
        return cursor.fetchone()
