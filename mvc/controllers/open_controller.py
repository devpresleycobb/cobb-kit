from events.event_manager import EventManager


class OpenController:

    def __init__(self, open_prs):
        self.__events = EventManager()
        self.open_prs = open_prs()

    def show(self, name: str = None):
        return self.open_prs.all(name=name)
