from abc import ABC, abstractmethod
from typing import Any

class ChainHandler(ABC):
    """
    Interface Handler para o padrão Chain Of Responsability. Todas as classes "AbstractChainHandler" devem ser oriundas desta classe.
    """

    @abstractmethod
    def set_next(self, handler: Any) -> Any:
        """
        handler deve ser uma implementação de ChainHandler e Any, da mesma forma este método deve retornar uma implementação de ChainHandler. Por alguma razão o Python acusa um erro dizendo que a classe ChainHandler não existe neste contexto, acredito que ele não consiga interpretar este tipo de chamada da propria classe em um de seus metodos.
        """
        pass

    @abstractmethod
    def handle(self, request:Any) -> Any|None:
        pass