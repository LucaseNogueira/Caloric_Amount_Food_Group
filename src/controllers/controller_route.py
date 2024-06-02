from abc import ABC, abstractmethod

class ControllerRoute(ABC):

    @abstractmethod
    def execute(self)->dict:
        pass