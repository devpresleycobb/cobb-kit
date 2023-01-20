from abc import ABC, abstractmethod


class EventListener(ABC):

    @abstractmethod
    def update(self, key, data, rerender):
        pass

    @property
    @abstractmethod
    def event_type(self):
        pass
