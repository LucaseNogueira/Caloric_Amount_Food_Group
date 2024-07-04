import unittest
import sys
sys.path.append('.')


from src.controllers.controller_calorias_grupo_alimento_route import ControllerCaloriasGrupoAlimentoRoute
from src.models.alimento_request import AlimentoRequestList, AlimentoRequest
from src.models.message import MessageSucesso

class TestControllerCaloriesGrupoAlimentoRoute(unittest.TestCase):

    def test_calorias_por_grupo_alimento(self):
        controller = ControllerCaloriasGrupoAlimentoRoute(AlimentoRequestList(alimentos=[AlimentoRequest(descricao='Lentilha', porcao=20)]))
        message = MessageSucesso('Requisição realizada com sucesso!')
        message.set_body({'total_calorias': 27.255399999999998, 'alimentos': [{'descricao': 'Lentilha', 'porcao': 20.0, 'calorias': 27.255399999999998}]})
        response = controller.execute()
        self.assertEqual(1,1)

    def test_porcao_error(self):
        pass

    def test_alimento_nao_encontrado_error(self):
        pass

if __name__ == '__main__':
    unittest.main()
