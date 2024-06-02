import unittest
import sys
sys.path.append('.')

from src.models.alimento_request import AlimentoRequestList, AlimentoRequest
from src.controllers.controller_api import ControllerApi

class TestControllerApi(unittest.TestCase):

    def test_calorias_por_grupo_alimento(self):
        alimento_list = AlimentoRequestList(alimentos=[AlimentoRequest(descricao='Lentilha', porcao=20)])

        controller = ControllerApi()
        alimento_list_dict = controller.get_calorias_por_grupo_alimentos(alimento_list)
        compare = {'total_calorias': 27.255399999999998, 'alimentos': [{'descricao': 'Lentilha', 'porcao': 20.0, 'calorias': 27.255399999999998}]}
        self.assertEqual(compare,alimento_list_dict)

    def test_porcao_invalida(self):
        alimento_list = AlimentoRequestList(alimentos=[AlimentoRequest(descricao='Lentilha', porcao=0)])

        controller = ControllerApi()
        with self.assertRaises(ValueError) as contexto:
            controller.get_calorias_por_grupo_alimentos(alimento_list)

        self.assertEqual(str(contexto.exception), "Informe um valor de porção maior que zero ou não informe um valor de porção (dado não obrigatório)")

    def test_alimento_nao_encontrada(self):
        descricao_alimento = 'Tenis'
        alimento_list = AlimentoRequestList(alimentos=[AlimentoRequest(descricao=descricao_alimento)])

        controller = ControllerApi()
        with self.assertRaises(ValueError) as contexto:
            controller.get_calorias_por_grupo_alimentos(alimento_list)

        self.assertEqual(str(contexto.exception), f'Não foi encontrado um alimento com o nome {descricao_alimento}')

if __name__ == '__main__':
    unittest.main()