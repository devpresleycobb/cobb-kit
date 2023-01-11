import sqlite3
from sql import create_repositories_sql
import os


class Database:
    __instance = None
    DATABASE_PATH = "database/database.db"

    def __init__(self):
        self.conn = sqlite3.connect(Database.DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.create_database()
        self.create_tables()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def create_tables(self):
        for sql in [create_repositories_sql]:
            self.cursor.executescript(sql)
            self.conn.commit()

    def __del__(self):
        self.conn.close()

    def create_database(self):
        """
        If the database does not exist, create it.
        """
        if not os.path.exists(Database.DATABASE_PATH):
            open(Database.DATABASE_PATH, "w").close()

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database.__instance = Database()
        return Database.__instance
