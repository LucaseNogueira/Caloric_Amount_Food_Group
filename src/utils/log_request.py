import traceback

from src.utils.interfaces.log_request_interface import LogRequestInterface
from datetime import datetime
from src.models.message import Message
from src.utils.string_utils import StringUtils
from src.utils.file_utils import FileUtils

class LogRequest(LogRequestInterface):

    def __init__(self, message:Message):
        self._data_hora = datetime.now()
        self._message = message
        self._trace = traceback.format_exc()

    @property
    def date_time(self):
        return self._data_hora

    @property
    def message(self):
        return self._message

    @property
    def trace(self):
        return self._trace

    @property
    def cadastrar(self):
        data_hora = str(self.date_time)
        conteudo = f"Data Hora: {data_hora}\n"
        subs = [{'old':':','new':'-'},{'old':'.','new':' '}]
        data_hora_titulo = StringUtils.replace(subs, data_hora)
        conteudo += f"Request Message: {str(self.message.to_dict)}\n"
        conteudo += f"Traceback: {str(self.trace)}"

        try:
            file_utils = FileUtils('/temp/log request', f'Log {data_hora_titulo}.txt', conteudo)
            file_utils.escrever_arquivo()
        except Exception as exc:
            print(str(exc))