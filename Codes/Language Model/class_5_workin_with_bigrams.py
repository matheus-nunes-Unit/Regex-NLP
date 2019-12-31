from nltk.util import bigrams
from nltk.lm.preprocessing import pad_both_ends

#Retirando os bigramas do texto teste
textos_teste = "Alura"
bigrama_texto_teste = bigrams(textos_teste)
print("Bigram of {} => {}".format(textos_teste,list(bigrama_texto_teste)))

'''
Adicionando fake chars no primeiro e no ultimo caracter do bigrama, para que assim a quantidade de caracteres fique a mesma
para todos os caracteres da frase e assim posssamos indetificar facilmente os caracteres de inicio e fim da sentença.
'''
padded_bigram = list(bigrams(pad_both_ends(textos_teste,n=2)))
print("Padded bigram => {}".format(padded_bigram))
