from abc import ABC, abstractmethod


class Apps(ABC):

    @abstractmethod
    def initialize(self):
        pass
