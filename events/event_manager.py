from singleton import singleton
from events.event_listener import EventListener


@singleton
class EventManager:

    def __init__(self):
        self.__observers = set()

    def subscribe(self, observer: EventListener):
        self.__observers.add(observer)

    def unsubscribe(self, observer: EventListener):
        self.__observers.remove(observer)

    def notify(self, event_type, rerender=True, key=None, data=None):
        for observer in self.__observers:
            if observer.event_type == event_type:
                observer.update(key=key, data=data, rerender=rerender)
