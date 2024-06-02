import unittest
import sys
sys.path.append('.')

from src.models.alimento import Alimento, AlimentoEnum

class TestAlimento(unittest.TestCase):

    def setUp(self):
        self.alimento = Alimento(1234,'Carne Teste',200.0)

    def test_atualiza_porcao_e_calorias(self):
        self.alimento.atualiza_porcao_e_calorias(200)
        self.assertEqual(200,self.alimento.porcao)
        self.assertEqual(400,self.alimento.calorias)

    def test_getters_alimento(self):
        self.assertEqual(1234, self.alimento.codigo)
        self.assertEqual('Carne Teste', self.alimento.descricao)
        self.assertEqual(200.0, self.alimento.calorias)
        self.assertEqual(AlimentoEnum.PORCAO_PADRAO.value, self.alimento.porcao)

if __name__ == '__main__':
    unittest.main()