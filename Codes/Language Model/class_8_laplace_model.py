import pandas as pd
from sklearn.model_selection import train_test_split 
from nltk.tokenize import WhitespaceTokenizer
from nltk.lm.preprocessing import padded_everygram_pipeline,pad_both_ends
from nltk.lm import Laplace
from nltk.util import bigrams
from pprint import pprint

def treinando_modelo_Laplace(lista_de_textos):
    #Salvando todas as frases em uma unica variavel
    todas_as_questoes = " ".join(lista_de_textos)
    #Separando as palavras do texto levando em consideração o espaço em branco
    todas_as_palavras = WhitespaceTokenizer().tokenize(todas_as_questoes)
    #Adicionando os fake chars em cada palavra e gerando o vetor de vocabulos(nesse caso letras de cada palavra)
    treino_bigram,vocab = padded_everygram_pipeline(2,todas_as_palavras)    
    #Criando modelo MLE para bigramas
    modelo = Laplace(2)
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

'''
Funcao responsavel por dada uma lista de textos e uma lista de idiomas, dizer o idioma de cada texto levando em consideracao
a menor perplexidade para cada texto. Sera retornado um vetor de string contendo o idioma de cada texto da lista de textos.
OBS: A lista de modelos passada tera que esta em uma ordem fixa(modelo em pt | modelo em ingles | modelo em espanhol) e
contendo no maximo tres idiomas(portugues, ingles e espanhol).
'''
def definir_idioma(lista_de_modelos,lista_de_textos):
    modelo_pt = lista_de_modelos[0]
    modelo_en = lista_de_modelos[1]
    modelo_esp = lista_de_modelos[2]

    #Vetor que ira armazenar o idioma de cada texto
    idiomas = []
    for texto in lista_de_textos:
        #Recebendo as perplexidades para cada idioma
        portugues = calcular_perplexidade(modelo_pt,texto)
        ingles = calcular_perplexidade(modelo_en,texto)
        espanhol = calcular_perplexidade(modelo_esp,texto)

        if ingles >= portugues <= espanhol:
            idiomas.append("portugues")
        elif portugues >= ingles <= espanhol:
            idiomas.append("ingles")
        else:
            idiomas.append("espanhol")

    return idiomas

if __name__ == "__main__":
    #Carregando base de dados
    dados_portugues = pd.read_csv("../data_sets/stackoverflow_portugues.csv")
    dados_ingles = pd.read_csv("../data_sets/stackoverflow_ingles.csv")
    dados_espanhol = pd.read_csv("../data_sets/stackoverflow_espanhol.csv")
    #Gerando dados de treino e teste
    pt_treino,pt_teste = train_test_split(dados_portugues["questoes tratadas"],test_size = 0.2,random_state = 123)
    en_treino,en_teste = train_test_split(dados_ingles["questoes tratadas"],test_size = 0.2,random_state = 123)
    esp_treino,esp_teste = train_test_split(dados_espanhol["questoes tratadas"],test_size = 0.2,random_state = 123)
    #Criando modelos de laplace
    modelo_pt_laplace = treinando_modelo_Laplace(pt_treino)
    modelo_ingles_laplace = treinando_modelo_Laplace(en_treino)
    modelo_esp_laplace = treinando_modelo_Laplace(esp_treino)
    #Demonstrando que a perplexidade infinita foi suavizada atraves do modelo de laplace
    print(calcular_perplexidade(modelo_ingles_laplace,pt_teste.iloc[0]))
    print(calcular_perplexidade(modelo_esp_laplace,pt_teste.iloc[0]))
    print(calcular_perplexidade(modelo_pt_laplace,pt_teste.iloc[0]))
    #Verificando o idioma de cada conjunto de textos de teste
    lista_de_modelos = [modelo_pt_laplace,modelo_ingles_laplace,modelo_esp_laplace]
    resultados_pt = definir_idioma(lista_de_modelos,pt_teste)
    resultados_en = definir_idioma(lista_de_modelos,en_teste)
    resultados_esp = definir_idioma(lista_de_modelos,esp_teste)
    #Calculando a taxa de acerto de cada modelo em porcentagem
    taxa_pt = (resultados_pt.count("portugues")/len(resultados_pt)*100)
    taxa_en = (resultados_en.count("ingles")/len(resultados_en)*100)
    taxa_esp = (resultados_esp.count("espanhol")/len(resultados_esp)*100)

    print("A taxa de acerto em portugues foi de {}".format(taxa_pt))
    print("A taxa de acerto em ingles foi de {}".format(taxa_en))
    print("A taxa de acerto em espanhol foi de {}".format(taxa_esp))