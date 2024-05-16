from abc import ABC, abstractmethod

class ResponseInterface(ABC):

    @abstractmethod
    def to_dict(self)->dict:
        pass