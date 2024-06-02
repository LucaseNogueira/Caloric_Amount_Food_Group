import sys, pandas as pd

sys.path.append('.')

from src.models.alimento import Alimento
from src.utils.string_utils import StringUtils

class ControllerAlimentoMeta(type):
    """
    Usando o conceito de metaclasse para aplicar o padrão Singleton na classe ControllerAlimento. É importante termos um Singleton nesta classe pois ela conversa com o arquivo CSV e instanciar este arquivo consome memória. Uma forma de evitar este consumo é utilizando o Singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ControllerAlimento(metaclass=ControllerAlimentoMeta):

    def __init__(self):
        self._df = pd.read_csv('data/Taco_Calorias_Alimentos.csv')

    def filtrar(self, frase:str)->Alimento|None:
        frase = StringUtils.sanitizar(frase)
        df_linha = None
        alimento = None
        if len(frase.split(' ')) == 1:
            df_linha = self._df.loc[self._df['Campo de Pesquisa'].str.startswith(frase, na=False)].head(1).sort_index(ignore_index=True)
        else:
            str_regex = '^'
            for str_aux in frase.split(' '):
                str_regex += str_aux + '.*'
            df_linha = self._df.loc[self._df['Campo de Pesquisa'].str.contains(str_regex)].head(1).sort_index(ignore_index=True)
        if not df_linha.empty:
            alimento = Alimento(df_linha['Código do alimento'][0], df_linha['Descrição do alimento'][0], df_linha['Calorias'][0])
        return alimento