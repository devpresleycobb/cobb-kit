from abc import ABC, abstractmethod


class Controller(ABC):

    @staticmethod
    @abstractmethod
    def show(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def store(name: str):
        pass

    @staticmethod
    @abstractmethod
    def delete():
        pass

    @staticmethod
    @abstractmethod
    def index():
        pass
