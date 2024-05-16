import sys, pandas as pd

sys.path.append('.')

from src.models.alimento import Alimento
from src.utils.string_utils import StringUtils

class ControllerAlimento:

    _instance = None

    def __init__(self):
        self._df = pd.read_csv('data/Taco_Calorias_Alimentos.csv')

    #def __new__(cls, *args, **kwargs):
    #    if not hasattr(cls, '_instance'):
    #        cls._instance = super().__new__(cls, *args, **kwargs)
    #    return cls._instance

    #@property
    #def instance(self):
    #    return self._instance

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