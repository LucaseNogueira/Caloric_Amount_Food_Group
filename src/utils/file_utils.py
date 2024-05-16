from pathlib import Path, os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class FileUtils:

    def __init__(self, nome_diretorio:str='', nome_arquivo:str='', conteudo_arquivo:str=''):
        self.nome_diretorio = nome_diretorio
        self.nome_arquivo = nome_arquivo
        self.conteudo_arquivo = conteudo_arquivo

    def escrever_arquivo(self):
        self.criar_diretorio()
        nome_arquivo = f'{BASE_DIR}/{self.nome_diretorio}/{self.nome_arquivo}'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(self.conteudo_arquivo)

    def criar_diretorio(self):
        dir_name = f'{BASE_DIR}/{self.nome_diretorio}'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)