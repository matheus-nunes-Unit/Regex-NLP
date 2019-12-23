from class_1_loading_information import LoadingInformations
from pprint import pprint
import re
from timeit import timeit

informations = LoadingInformations()

questao = informations.getQuestao(2)

#Encontrando todas as tags html das questoes
tags_founded = re.findall(r"<.*?>",questao)
print(tags_founded)

#Substituindo as tags html por caracteres em branco
questao = re.sub(r"<.*?>","",questao)
pprint(questao)

#Testando metodo search
text =  "Ola mestre yoda."
print(re.search(r"yoda",text))

#Testando metodo compile e mostrando diferenca de tempo
setup_sem_compilar = """
import re
text = "Ola mestre yoda."
"""

setup_compilado = """
import re
text = "Ola mestre yoda."
compiled = re.compile(r"yoda")                
"""

print("Tempo sem compilar: {tempo}".format(tempo = timeit(setup= setup_sem_compilar,stmt="""re.search(r"yoda",text)""")))
print("Tempo compilado: {tempo}".format(tempo = timeit(setup= setup_compilado,stmt="""compiled.search(text)""")))