import re
from class_1_loading_information import LoadingInformations
from pprint import pprint
from IPython.display import display, HTML
import webbrowser
import pandas as pd
from tempfile import NamedTemporaryFile

#Gerando tabela html
def df_window(df):
    with NamedTemporaryFile(delete=False, suffix='.html',mode="w", encoding="utf-8") as f:
        df.to_html(f)
    webbrowser.open(f.name)

#Função para substituir os caracteres definidos da regex por espaço em branco no(s) texto(s)
def remover(textos,regex):
    if type(textos) == str:
        return regex.sub("",textos)
    else:
        return [regex.sub("",texto) for texto in textos]

#Funcao para substituir as tags e os codigos dentro das mesmas por CODE
def substituir(textos,regex):
    if type(textos) == str:
        return regex.sub("CODE",textos)
    else:
        return [regex.sub("CODE",texto) for texto in textos]
        
if __name__ == "__main__":
    data = LoadingInformations()
    dados_pt = data.dados_portugues.Questão
    dados_en = data.dados_ingles.Questão
    dados_es = data.dados_espanhol.Questão

    #Regex para remover as tags code e os seus respectivos codigos
    regex_code = re.compile(r"<code>(.|(\n))*?</code>")
    #Regex para remover as tags html
    regex_html = re.compile(r"<.*?>")

    #Removendo tag code e o codigo dos dados em portugues
    dados_sem_code_pt = substituir(dados_pt,regex_code)
    #Removendo tags html dos dados em portugues
    dados_sem_code_html_pt = remover(dados_sem_code_pt,regex_html)
    #criando nova coluna no dataframe
    data.add_coluna_pt("sem_code_tag",dados_sem_code_html_pt)

    #Removendo tag code e o codigo dos dados em ingles
    dados_sem_code_en = substituir(dados_en,regex_code)
    #Removendo tags html dos dados em ingles
    dados_sem_code_html_en = remover(dados_sem_code_en,regex_html)
    #criando nova coluna no dataframe
    data.add_coluna_en("sem_code_tag",dados_sem_code_html_en)

    #Removendo tag code e o codigo dos dados em espanhol
    dados_sem_code_es = substituir(dados_es,regex_code)
    #Removendo tags html dos dados em espanhol
    dados_sem_code_html_es = remover(dados_sem_code_es,regex_html)
    #criando nova coluna no dataframe
    data.add_coluna_es("sem_code_tag",dados_sem_code_html_es)

    #Codigo opcional para gerar arquivos com as tabelas de dados
    #df_window(data.dados_portugues)
    #df_window(data.dados_ingles)
    #df_window(data.dados_espanhol)