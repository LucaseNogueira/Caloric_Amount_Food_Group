from src.models.interfaces.message_interface import MessageInterface
from src.models.interfaces.response_interface import ResponseInterface
from http import HTTPStatus
from datetime import datetime

class Message(MessageInterface, ResponseInterface):
    
    _status_code: int

    def __init__(self, mensagem:str):
        self._mensagem = mensagem
        self._body = None
        self._data_hora = datetime.now()
    
    @property
    def status_code(self):
        return self._status_code
    
    @property
    def mensagem(self):
        return self._mensagem
    
    @property
    def body(self):
        return self._body
    
    @property
    def data_hora(self):
        return self._data_hora

    @property
    def to_dict(self)->dict:
        return {
            'status_code':self.status_code,
            'data_hora':str(self.data_hora),
            'mensagem':self.mensagem,
            'body':self.body
        }
    
    def set_body(self, body):
        self._body = body

class MessageSucesso(Message):

    def __init__(self, mensagem: str):
        self._status_code = HTTPStatus.OK
        super().__init__(mensagem)

class MessageNotFound(Message):

    def __init__(self, mensagem: str):
        self._status_code = HTTPStatus.NOT_FOUND
        super().__init__(mensagem)

class MessageInternaServerlError(Message):

    def __init__(self, mensagem: str):
        self._status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        super().__init__(mensagem)
