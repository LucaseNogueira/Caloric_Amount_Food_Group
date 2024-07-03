from typing import Any
from src.utils.chian_handler import ChainHandler
from src.models.message import MessageNotFound, MessageInternaServerlError
from src.utils.log_request import LogRequest

class ExceptionAbstractChainHandler(ChainHandler):

    _next_handler: ChainHandler = None

    def set_next(self, handler: ChainHandler) -> ChainHandler:
        self._next_handler = handler
        return handler
    
    def handle(self, request: Any) -> Any | None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
    
class ValueErrorChainHandler(ExceptionAbstractChainHandler):

    def handle(self, request: Any) -> Any | None:
        if isinstance(request, ValueError):
            message = MessageNotFound(str(request))
            ##log = LogRequest(message)
            ##log.cadastrar
            return message.to_dict
        else:
            return super().handle(request)

class ExceptionChainHandler(ExceptionAbstractChainHandler):

    def handle(self, request: Any) -> Any | None:
        if isinstance(request, Exception):
            message = MessageInternaServerlError('Ocorreu uma falha interna no servidor')
            ##log = LogRequest(message)
            ##log.cadastrar
            return message.to_dict
        else:
            return super().handle(request)