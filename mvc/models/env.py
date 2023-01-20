from dotenv import dotenv_values, set_key
from events.event_manager import EventManager
import os


class Env:

    events = None
    PATH = '.env'

    def __init__(self):
        self.events = EventManager()

    def get_key_by_name(self, name):
        return dotenv_values(".env").get(name, '')

    def set_key_by_name(self, name, value):
        if not os.path.exists(Env.PATH):
            with open(Env.PATH, 'w') as f:
                f.write(f"{name}='{value}'")
        else:
            set_key(".env", name, value)
        self.events.notify('settings')
