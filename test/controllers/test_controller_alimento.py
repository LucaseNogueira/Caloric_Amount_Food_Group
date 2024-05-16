import unittest
import sys
sys.path.append('.')

from src.controllers.controller_alimento import ControllerAlimento
from src.models.alimento import Alimento

class TestControllerAlimento(unittest.TestCase):

    def setUp(self) -> None:
        self._controller = ControllerAlimento()

    def test_filtrar(self):
        descricao_alimento = 'Canjiquinha de milho em grão'
        alimento = Alimento(6300706,descricao_alimento,79.68)
        self.assertEqual(alimento, self._controller.filtrar(descricao_alimento))

    def test_filtrar_none(self):
        descricao_alimento = 'O aluguel da Kombi do Tião ta muito caro gente'
        self.assertIsNone(self._controller.filtrar(descricao_alimento))

if __name__ == '__main__':
    unittest.main()