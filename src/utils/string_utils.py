import re, nltk, unicodedata

nltk.download('stopwords')
from nltk.corpus import stopwords

class StringUtils:

    @staticmethod
    def sanitizar(frase:str)->str:
        sw = stopwords.words('portuguese')
        str_processada = re.sub(r"[,.()]", "", frase)
        str_processada = str_processada.replace('etc','')
        str_processada = ' '.join([k for k in str_processada.split(" ") if k not in sw])
        str_processada = str_processada.upper()
        str_processada = unicodedata.normalize("NFD", str_processada)
        str_processada = str_processada.encode("ascii", "ignore").decode("utf-8").strip()
        str_processada = re.sub(r"[^A-Z0-9]", " ", str_processada)
        return str_processada
    
    @staticmethod
    def replace(subs:list, artigo:str)->str:
        for sub in subs:
            artigo = artigo.replace(sub['old'], sub['new'])
        return artigo