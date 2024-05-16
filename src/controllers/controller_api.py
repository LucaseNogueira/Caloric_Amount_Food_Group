import json

from src.models.alimento_request import AlimentoRequestList
from src.models.alimento_response import AlimentoResponseList, AlimentoResponse
from src.controllers.controller_alimento import ControllerAlimento

class ControllerApi:
    
    @classmethod
    def get_calorias_por_grupo_alimentos(self, alimentos:AlimentoRequestList):
        controller_alimento = ControllerAlimento()
        alimento_response_list = AlimentoResponseList()
        for alimento_request in alimentos.alimentos:
            alimento_filtrado = controller_alimento.filtrar(alimento_request.descricao)
            if alimento_filtrado:
                if alimento_request.porcao <= 0:
                    raise ValueError('Informe um valor de porção maior que zero ou não informe um valor de porção (dado não obrigatório)')
                if alimento_request.porcao != alimento_filtrado.porcao:
                    alimento_filtrado.atualiza_porcao_e_calorias(alimento_request.porcao)
                alimento_response = AlimentoResponse(alimento_filtrado.descricao, alimento_filtrado.porcao, alimento_filtrado.calorias)
                alimento_response_list.total_calorias += alimento_filtrado.calorias
                alimento_response_list.alimentos.append(alimento_response)
            else:
                raise ValueError('Não foi encontrado um alimento com o nome ' + alimento_request.descricao)
        return alimento_response_list.to_dict