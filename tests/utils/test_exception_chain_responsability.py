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
        self.assertEqual(1,1)

    def test_exception_chain_handler(self):
        message = MessageInternaServerlError("Ocorreu uma falha interna no servidor")
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
