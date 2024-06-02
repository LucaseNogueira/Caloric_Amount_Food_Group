from src.controllers.controller_route import ControllerRoute
from pydantic import BaseModel
from src.controllers.controller_api import ControllerApi
from src.utils.exception_chain_responsability import ValueErrorChainHandler, ExceptionChainHandler
from src.models.message import MessageSucesso
from src.controllers.controller_consumer_service import ControllerConsumerServiceGETMethod

class ControllerCaloriasGrupoAlimentoRoute(ControllerRoute):

    def __init__(self, payload:BaseModel, token:str=None)->None:
        self._payload = payload

    def execute(self) -> dict:
        try:
            validaToken(token)
            alimentos_json = ControllerApi.get_calorias_por_grupo_alimentos(self._payload)
            message = MessageSucesso('Requisição realizada com sucesso!')
            message.set_body(alimentos_json)
            return message.to_dict
        except Exception as e:
            value_error = ValueErrorChainHandler()
            exception_padrao = ExceptionChainHandler()
            value_error.set_next(exception_padrao)

            return value_error.handle(e)
    
    def validaToken(self,token):
        response = ControllerConsumerServiceGETMethod('http://auth:8080/auth/validate', token)
        if response == False:
            raise ValueError('O token informado é invalido')
        return response

