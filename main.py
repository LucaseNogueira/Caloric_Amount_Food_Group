from fastapi import FastAPI, Request
from src.models.alimento_request import AlimentoRequestList
from src.controllers.controller_api import ControllerApi
from src.models.message import MessageSucesso, MessageNotFound, MessageInternaServerlError
from src.utils.log_request import LogRequest

app = FastAPI()

@app.post('/foodgroup/')
async def get_calorias_por_grupo_alimentos(alimentos:AlimentoRequestList):
    try:
        alimentos_json = ControllerApi.get_calorias_por_grupo_alimentos(alimentos)
        message = MessageSucesso('Requisição realizada com sucesso!')
        message.set_body(alimentos_json)
        return message.to_dict
    except ValueError as e:
        message = MessageNotFound(str(e))
        log = LogRequest(message)
        log.cadastrar
        return message.to_dict
    except Exception as e:
        message = MessageInternaServerlError('Ocorreu uma falha interna no servidor')
        log = LogRequest(message)
        log.cadastrar
        return message.to_dict