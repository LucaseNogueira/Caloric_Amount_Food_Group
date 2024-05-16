from enum import Enum

class Alimento:

    def __init__(self,codigo:int,descricao:str,calorias:float):
        self._codigo = codigo
        self._descricao = descricao
        self._calorias = calorias
        self._porcao = AlimentoEnum.PORCAO_PADRAO.value

    @property
    def codigo(self):
        return self._codigo
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def calorias(self):
        return self._calorias
    
    @property
    def porcao(self):
        return self._porcao

    def atualiza_porcao_e_calorias(self, porcao):
        self._calorias = self._calorias * (porcao/self._porcao)
        self._porcao = porcao

class AlimentoEnum(Enum):
    PORCAO_PADRAO = 100.00