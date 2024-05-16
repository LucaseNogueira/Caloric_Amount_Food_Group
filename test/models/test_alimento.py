import unittest
import sys
sys.path.append('.')

from src.models.alimento import Alimento

class TestAlimento(unittest.TestCase):

    def setUp(self):
        self.alimento = Alimento(1234,'Carne Teste',200.0)

    def test_atualiza_porcao_e_calorias(self):
        self.alimento.atualiza_porcao_e_calorias(200)
        self.assertEqual(200,self.alimento.porcao)
        self.assertEqual(400,self.alimento.calorias)

if __name__ == '__main__':
    unittest.main()