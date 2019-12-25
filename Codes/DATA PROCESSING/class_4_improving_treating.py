from class_1_loading_information import LoadingInformations
from class_3_treating_data_web import TreatedData
import re

class TotalTreatment:

    ''' 
    O metodo init ira bascimanete realizar o tratamento final dos dados e adicionalos como uma coluna nova no csv
    '''
    def __init__(self):
        default_info = LoadingInformations()
        treated_data = TreatedData()
        dados_tratados_pt = treated_data.dados_sem_code_html_pt
        dados_tratados_en = treated_data.dados_sem_code_html_en
        dados_tratados_es = treated_data.dados_sem_code_html_es

        #Regex para retirada de caracteres alfanumericos(pontuação). Sera evitado que sejam retirados os espaços atarves do /s
        regex_pontuacao = re.compile(r"[^\w\s]")
        #Regex para retirada de multiplos espacos
        regex_multiplos_espacos = re.compile(r" +")
        #Regex para remover multiplas quebra de linha
        regex_quebra_linha = re.compile(r"(\n)+")
        #Regex para remover os digitos
        regex_digitos = re.compile(r"\d+")

        #Removendo pontuacao das questoes
        questoes_pt_sem_pont = treated_data.remover(dados_tratados_pt,regex_pontuacao)
        questoes_en_sem_pont = treated_data.remover(dados_tratados_en,regex_pontuacao)
        questoes_es_sem_pont = treated_data.remover(dados_tratados_es,regex_pontuacao)

        #Colocando as questoes em minusculo
        questoes_pt_sem_pont_minus = self.minusculo(questoes_pt_sem_pont,regex_pontuacao)
        questoes_en_sem_pont_minus = self.minusculo(questoes_en_sem_pont,regex_pontuacao)
        questoes_es_sem_pont_minus = self.minusculo(questoes_es_sem_pont,regex_pontuacao)

        #Removendo os numerais das questoes
        questoes_pt_sem_numerais = treated_data.remover(questoes_pt_sem_pont_minus,regex_digitos)
        questoes_en_sem_numerais = treated_data.remover(questoes_en_sem_pont_minus,regex_digitos)
        questoes_es_sem_numerais = treated_data.remover(questoes_es_sem_pont_minus,regex_digitos)

        #Retirando multiplas quebras de linhas
        questoes_pt_sem_quebra_linha= self.substituir_por_espaco(questoes_pt_sem_numerais,regex_quebra_linha)
        questoes_en_sem_quebra_linha = self.substituir_por_espaco(questoes_en_sem_numerais,regex_quebra_linha)
        questoes_es_sem_quebra_linha = self.substituir_por_espaco(questoes_es_sem_numerais,regex_quebra_linha)

        #Retirando espaco duplicado das questoes
        self.__questoes_pt_sem_espaco_dup__ = self.substituir_por_espaco(questoes_pt_sem_quebra_linha,regex_multiplos_espacos)
        self.__questoes_en_sem_espaco_dup__ = self.substituir_por_espaco(questoes_en_sem_quebra_linha,regex_multiplos_espacos)
        self.__questoes_es_sem_espaco_dup__ = self.substituir_por_espaco(questoes_es_sem_quebra_linha,regex_multiplos_espacos)

        #Adicionando Modificacoes na planilha como uma nova coluna
        default_info.add_coluna_pt("questoes tratadas",self.__questoes_pt_sem_espaco_dup__)
        default_info.add_coluna_en("questoes tratadas",self.__questoes_en_sem_espaco_dup__)
        default_info.add_coluna_es("questoes tratadas",self.__questoes_es_sem_espaco_dup__)

    #Funcao para deixar o texto minusculo
    @staticmethod
    def minusculo(textos,regex):
        if type(textos) == str:
            return textos.lower()
        else:
            return [texto.lower() for texto in textos]
    @staticmethod
    def substituir_por_espaco(textos,regex):
        if type(textos) == str:
            return regex.sub(" ",textos)
        else:
            return [regex.sub(" ",texto) for texto in textos]

    @property
    def questoes_pt(self):
        return self.__questoes_pt_sem_espaco_dup__

    @property
    def questoes_en(self):
        return self.__questoes_en_sem_espaco_dup__

    @property
    def questoes_es(self):
        return self.__questoes_es_sem_espaco_dup__

if __name__ == "__main__":
    questoes_tratadas = TotalTreatment()    
    print(questoes_tratadas.questoes_pt)