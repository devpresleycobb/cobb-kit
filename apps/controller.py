from abc import ABC, abstractmethod


class Controller(ABC):

    @staticmethod
    @abstractmethod
    def show():
        pass

    @staticmethod
    @abstractmethod
    def store():
        pass

    @staticmethod
    @abstractmethod
    def update():
        pass

    @staticmethod
    @abstractmethod
    def delete():
        pass
