from abc import ABC, abstractmethod


class Apps(ABC):

    @staticmethod
    @abstractmethod
    def initialize(root):
        pass
