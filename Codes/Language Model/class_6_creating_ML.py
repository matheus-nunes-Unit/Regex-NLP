import pandas as pd
from sklearn.model_selection import train_test_split 
from nltk.tokenize import WhitespaceTokenizer
from nltk.lm.preprocessing import padded_everygram_pipeline,pad_both_ends
from nltk.lm import MLE
from nltk.util import bigrams
from pprint import pprint

dados_portugues = pd.read_csv("../data_sets/stackoverflow_portugues.csv")
dados_ingles = pd.read_csv("../data_sets/stackoverflow_ingles.csv")
dados_espanhol = pd.read_csv("../data_sets/stackoverflow_espanhol.csv")

# #Criando coluna idioma de cada um dos data frame de dados
# dados_portugues["Idioma"] = "Portugues"
# dados_ingles["Idioma"] = "Ingles"
# dados_espanhol["Idioma"] = "Espanhol"
# #Passando a coluna Idioma para o csv
# dados_portugues.to_csv("../data_sets/stackoverflow_portugues.csv")
# dados_ingles.to_csv("../data_sets/stackoverflow_ingles.csv")
# dados_espanhol.to_csv("../data_sets/stackoverflow_espanhol.csv")

#Gerando dados de treino e teste
pt_treino,pt_teste = train_test_split(dados_portugues["questoes tratadas"],test_size = 0.2,random_state = 123)
en_treino,pt_teste = train_test_split(dados_ingles["questoes tratadas"],test_size = 0.2,random_state = 123)
esp_treino,pt_teste = train_test_split(dados_espanhol["questoes tratadas"],test_size = 0.2,random_state = 123)

#Salvando todas as frases em uma unica variavel
todas_as_frases_pt = " ".join(pt_treino)
todas_as_frases_en = " ".join(en_treino)
todas_as_frases_esp = " ".join(esp_treino)

#Separando as palavras do texto levando em consideração o espaço em branco
todas_as_palavras_pt = WhitespaceTokenizer().tokenize(todas_as_frases_pt)
todas_as_palavras_en = WhitespaceTokenizer().tokenize(todas_as_frases_en)
todas_as_palavras_esp = WhitespaceTokenizer().tokenize(todas_as_frases_esp)

#Adicionando os fake chars em cada palavra e gerando o vetor de vocabulos(nesse caso letras de cada palavra)
port_treino_bigram,vocab_port = padded_everygram_pipeline(2,todas_as_palavras_pt)
engl_treino_bigram,vocab_engl = padded_everygram_pipeline(2,todas_as_palavras_en)
espa_treino_bigram,vocab_espa = padded_everygram_pipeline(2,todas_as_palavras_esp)

#Criando modelo MLE para bigramas
modelo_port = MLE(2)
modelo_eng = MLE(2)
modelo_esp = MLE(2)

#Treinando os modelos
modelo_port.fit(port_treino_bigram,vocab_port)
modelo_eng.fit(engl_treino_bigram,vocab_engl)
modelo_esp.fit(espa_treino_bigram,vocab_espa)

#Testando geração de palavras
print("Palavra aleatoria gerada para portugues {}".format(modelo_port.generate(num_words=4)))
print("Palavra aleatoria gerada para ingles {}".format(modelo_eng.generate(num_words=4)))
print("Palavra aleatoria gerada para espanhol {}".format(modelo_esp.generate(num_words=4)))

#Verificando dicionario de frequencia para letra m
print(modelo_port.counts[['m']].items())
print(modelo_eng.counts[['m']].items())
print(modelo_esp.counts[['m']].items())

#Testando de forma basica o modelo e verificando seu valor de perplexidade
texto = "bom dia"
palavras_texto = WhitespaceTokenizer().tokenize(texto)
palavras_com_fake_char = [list(pad_both_ends(palavra,n = 2)) for palavra in palavras_texto]
palavras_bigramas = [list(bigrams(palavra)) for palavra in palavras_com_fake_char]

print("Valor de perplexidade para a palavra bom: {}".format(modelo_port.perplexity(palavras_bigramas[0])))
print("Valor de perplexidade para a palavra dia: {}".format(modelo_port.perplexity(palavras_bigramas[1])))
