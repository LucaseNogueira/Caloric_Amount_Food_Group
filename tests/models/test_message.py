import unittest
import sys
sys.path.append('.')

from src.models.message import MessageInternaServerlError, MessageSucesso, MessageNotFound
from http import HTTPStatus

class TestMessage(unittest.TestCase):

    def setUp(self) -> None:
        self.message_internal_error = MessageInternaServerlError("Ocorreu um problema no servidor")
        self.message_sucesso = MessageSucesso("Requisição realizada com sucesso!")
        self.message_not_found = MessageNotFound("Não existe um alimento com a descrição informada.")

        self._body = {'teste':'Valor do teste'}
        self.message_internal_error.set_body(self._body)
        self.message_sucesso.set_body(self._body)
        self.message_not_found.set_body(self._body)

    def test_status_code(self):
        self.assertEqual(HTTPStatus.INTERNAL_SERVER_ERROR, self.message_internal_error.status_code)
        self.assertEqual(HTTPStatus.OK, self.message_sucesso.status_code)
        self.assertEqual(HTTPStatus.NOT_FOUND, self.message_not_found.status_code)

    def test_mensagem(self):
        self.assertEqual("Ocorreu um problema no servidor", self.message_internal_error.mensagem)
        self.assertEqual("Requisição realizada com sucesso!", self.message_sucesso.mensagem)
        self.assertEqual("Não existe um alimento com a descrição informada.", self.message_not_found.mensagem)

    def test_body(self):
        self.assertEqual(self._body, self.message_internal_error.body)
        self.assertEqual(self._body, self.message_sucesso.body)
        self.assertEqual(self._body, self.message_not_found.body)

    def test_data_hora(self):
        self.assertIsNotNone(self.message_internal_error.data_hora)
        self.assertIsNotNone(self.message_sucesso.data_hora)
        self.assertIsNotNone(self.message_not_found.data_hora)

if __name__ == '__main__':
    unittest.main()