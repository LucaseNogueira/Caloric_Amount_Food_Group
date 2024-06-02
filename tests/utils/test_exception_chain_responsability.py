import unittest
import sys
sys.path.append('.')

from src.utils.exception_chain_responsability import ExceptionChainHandler, ValueErrorChainHandler
from src.models.message import MessageNotFound, MessageInternaServerlError

class TextExceptionChainResposability(unittest.TestCase):

    def setUp(self) -> None:
        self._error = ValueErrorChainHandler()
        self._error.set_next(ExceptionChainHandler())

    def test_value_error_chain_handler(self):
        message = MessageNotFound("Valor invalido")
        try:
            raise ValueError(message.mensagem)
        except Exception as e:
            self.assertEqual(message.to_dict,self._error.handle(e))

    def test_exception_chain_handler(self):
        message = MessageInternaServerlError("Ocorreu uma falha interna no servidor")
        try:
            raise Exception('Testando')
        except Exception as e:
            self.assertEqual(message.to_dict,self._error.handle(e))

if __name__ == '__main__':
    unittest.main()