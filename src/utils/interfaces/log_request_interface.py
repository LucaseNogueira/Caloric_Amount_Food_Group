from abc import ABC, abstractmethod

class LogRequestInterface(ABC):

    @abstractmethod
    def date_time(self):
        pass

    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def trace(self):
        pass

    @abstractmethod
    def cadastrar(self):
        pass