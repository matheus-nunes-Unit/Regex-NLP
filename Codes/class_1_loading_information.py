import pandas as pd
from IPython.display import display

class LoadingInformations:

    def __init__(self):
        self.dados_portugues = pd.read_csv("data_sets/stackoverflow_portugues.csv")
        self.dados_ingles = pd.read_csv("data_sets/stackoverflow_ingles.csv")
        self.dados_espanhol = pd.read_csv("data_sets/stackoverflow_espanhol.csv")

    def getQuestao(self,numero_da_questao):
        if type(numero_da_questao) == int:
            return self.dados_portugues.Questão[numero_da_questao] 

if __name__ == "__main__":
    print("DATA PORTUGUESE")
    display(dados_portugues.head()) 

    print("DATA INGLES")
    display(dados_ingles.head())

    print("DATA ESPANHOL")
    display(dados_espanhol.head())