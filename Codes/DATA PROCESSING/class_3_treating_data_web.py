import re
from class_1_loading_information import LoadingInformations
from pprint import pprint
from IPython.display import display, HTML
import webbrowser
import pandas as pd
from tempfile import NamedTemporaryFile

class TreatedData:

    '''
    O init ira basicamente realizar o tratamento dos dados e criar uma coluna no data frame de cada lingua com os dados
    filtrados.
    ''' 
    def __init__(self):
        data = LoadingInformations()
        dados_pt = data.dados_portugues.Questão
        dados_en = data.dados_ingles.Questão
        dados_es = data.dados_espanhol.Questão

        #Regex para remover as tags code e os seus respectivos codigos
        regex_code = re.compile(r"<code>(.|(\n))*?</code>")
        #Regex para remover as tags html
        regex_html = re.compile(r"<.*?>")

        #Removendo tag code e o codigo dos dados em portugues
        dados_sem_code_pt = self.substituir(dados_pt,regex_code)
        #Removendo tags html dos dados em portugues
        self.__dados_sem_code_html_pt__ = self.remover(dados_sem_code_pt,regex_html)
        #criando nova coluna no dataframe
        data.add_coluna_pt("sem_code_tag",self.__dados_sem_code_html_pt__)

        #Removendo tag code e o codigo dos dados em ingles
        dados_sem_code_en = self.substituir(dados_en,regex_code)
        #Removendo tags html dos dados em ingles
        self.__dados_sem_code_html_en__ = self.remover(dados_sem_code_en,regex_html)
        #criando nova coluna no dataframe
        data.add_coluna_en("sem_code_tag",self.__dados_sem_code_html_en__)

        #Removendo tag code e o codigo dos dados em espanhol
        dados_sem_code_es = self.substituir(dados_es,regex_code)
        #Removendo tags html dos dados em espanhol
        self.__dados_sem_code_html_es__ = self.remover(dados_sem_code_es,regex_html)
        #criando nova coluna no dataframe
        data.add_coluna_es("sem_code_tag",self.__dados_sem_code_html_es__)

        #Copiando nova coluna para o csv

        #Codigo opcional para gerar arquivos html com as tabelas de dados
        #df_window(data.dados_portugues)
        #df_window(data.dados_ingles)
        #df_window(data.dados_espanhol)
    
    #Função para substituir os caracteres definidos da regex por espaço em branco no(s) texto(s)
    @staticmethod
    def remover(textos,regex):
        if type(textos) == str:
            return regex.sub("",textos)
        else:
            return [regex.sub("",texto) for texto in textos]

    #Funcao para substituir as tags e os codigos dentro das mesmas por CODE
    @staticmethod
    def substituir(textos,regex):
        if type(textos) == str:
            return regex.sub("CODE",textos)
        else:
            return [regex.sub("CODE",texto) for texto in textos]

    #Gerando tabela html
    @staticmethod
    def df_window(df):
        with NamedTemporaryFile(delete=False, suffix='.html',mode="w", encoding="utf-8") as f:
            df.to_html(f)
        webbrowser.open(f.name)

    #Metodos para retorno das informacoes tratadas
    @property
    def dados_sem_code_html_pt(self):
        return self.__dados_sem_code_html_pt__

    @property
    def dados_sem_code_html_en(self):
        return self.__dados_sem_code_html_en__

    @property
    def dados_sem_code_html_es(self):
        return self.__dados_sem_code_html_es__

if __name__ == "__main__":
    treated_info = TreatedData()

    #Dados
    pprint(treated_info.dados_sem_code_html_pt)
    pprint(treated_info.dados_sem_code_html_en)
    pprint(treated_info.dados_sem_code_html_es)