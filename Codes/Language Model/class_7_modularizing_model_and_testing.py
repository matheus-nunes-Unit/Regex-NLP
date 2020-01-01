import pandas as pd
from sklearn.model_selection import train_test_split 
from nltk.tokenize import WhitespaceTokenizer
from nltk.lm.preprocessing import padded_everygram_pipeline,pad_both_ends
from nltk.lm import MLE
from nltk.util import bigrams
from pprint import pprint

def treinando_modelo_MLE(lista_de_textos):
    #Salvando todas as frases em uma unica variavel
    todas_as_questoes = " ".join(lista_de_textos)
    #Separando as palavras do texto levando em consideração o espaço em branco
    todas_as_palavras = WhitespaceTokenizer().tokenize(todas_as_questoes)
    #Adicionando os fake chars em cada palavra e gerando o vetor de vocabulos(nesse caso letras de cada palavra)
    treino_bigram,vocab = padded_everygram_pipeline(2,todas_as_palavras)    
    #Criando modelo MLE para bigramas
    modelo = MLE(2)
    #Treinando os modelos
    modelo.fit(treino_bigram,vocab)

    return modelo

#Funcao responsavel para calcuklarmos a perplexidade de todas as palavras de uma determinada frase
def calcular_perplexidade(modelo,frase):
    palavras_texto = WhitespaceTokenizer().tokenize(frase)
    palavras_com_fake_char = [list(pad_both_ends(palavra,n = 2)) for palavra in palavras_texto]
    palavras_bigramas = [list(bigrams(palavra)) for palavra in palavras_com_fake_char]
    perplexidade = 0
    for palavra in palavras_bigramas:
        perplexidade += modelo.perplexity(palavra)

    return perplexidade
    
if __name__ == "__main__":
    #Carregando base de dados
    dados_portugues = pd.read_csv("../data_sets/stackoverflow_portugues.csv")
    dados_ingles = pd.read_csv("../data_sets/stackoverflow_ingles.csv")
    dados_espanhol = pd.read_csv("../data_sets/stackoverflow_espanhol.csv")
    #Gerando dados de treino e teste
    pt_treino,pt_teste = train_test_split(dados_portugues["questoes tratadas"],test_size = 0.2,random_state = 123)
    en_treino,en_teste = train_test_split(dados_ingles["questoes tratadas"],test_size = 0.2,random_state = 123)
    esp_treino,esp_teste = train_test_split(dados_espanhol["questoes tratadas"],test_size = 0.2,random_state = 123)
    #Gerando modelos a partir da função
    modelo_port = treinando_modelo_MLE(pt_treino)
    modelo_en = treinando_modelo_MLE(en_treino)
    modelo_esp = treinando_modelo_MLE(esp_treino)
    #Testando a perplexidade
    print(calcular_perplexidade(modelo_port,pt_teste.iloc[0]))
    #Demonstrando a perplexidade infinita
    print(calcular_perplexidade(modelo_en,pt_teste.iloc[0]))