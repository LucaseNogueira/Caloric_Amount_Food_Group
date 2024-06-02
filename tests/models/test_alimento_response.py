import unittest
import sys
sys.path.append('.')

from src.models.alimento_response import AlimentoResponse, AlimentoResponseList

class TestAlimentoResponse(unittest.TestCase):
    
    def setUp(self) -> None:
        self.alimento = AlimentoResponse('Fruta carne', 100, 53)

        self.alimento_list = AlimentoResponseList()
        self.alimento_list.total_calorias = 128
        self.alimento_list.alimentos.append(AlimentoResponse('Fruta vegetal', 12, 8))
        self.alimento_list.alimentos.append(AlimentoResponse('Fruta sopa', 230, 101))
        self.alimento_list.alimentos.append(AlimentoResponse('Fruta frutada', 22, 19))

    def test_alimento_to_dict(self):
        self.assertEqual({
            'descricao':'Fruta carne',
            'porcao':100,
            'calorias':53
        },self.alimento.to_dict)

    def test_alimento_list_to_dict(self):
        self.assertEqual({
            'total_calorias':128,
            'alimentos':[
                {
                    'descricao':'Fruta vegetal',
                    'porcao':12,
                    'calorias':8
                },
                {
                    'descricao':'Fruta sopa',
                    'porcao':230,
                    'calorias':101
                },
                {
                    'descricao':'Fruta frutada',
                    'porcao':22,
                    'calorias':19
                },
            ]
        },self.alimento_list.to_dict)

if __name__ == '__main__':
    unittest.main()