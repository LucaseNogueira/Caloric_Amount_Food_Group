from typing import List
from src.models.interfaces.response_interface import ResponseInterface

class AlimentoResponse(ResponseInterface):

    def __init__(self, descricao:str, porcao:float, calorias:float):
        self.descricao = descricao
        self.porcao = porcao
        self.calorias = calorias

    @property
    def to_dict(self)->dict:
        return {
            'descricao':self.descricao,
            'porcao':self.porcao,
            'calorias':self.calorias
        }

class AlimentoResponseList(ResponseInterface):

    def __init__(self):
        self.total_calorias = 0.0
        self.alimentos = list()

    @property
    def to_dict(self)->dict:
        lista_alimento = list()
        for alimento in self.alimentos:
            lista_alimento.append(alimento.to_dict)
        return {
            'total_calorias':self.total_calorias,
            'alimentos':lista_alimento
        }