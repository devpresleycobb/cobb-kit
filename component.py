from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def title(self):
        pass
