from abc import ABC, abstractmethod

class MessageInterface(ABC):
    
    @abstractmethod
    def status_code(self):
        pass

    @abstractmethod
    def mensagem(self):
        pass

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def set_body(self, body):
        pass

    @abstractmethod
    def data_hora(self):
        pass