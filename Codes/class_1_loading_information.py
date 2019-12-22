import pandas as pd
from IPython.display import display
dados_portugues = pd.read_csv("data_sets/stackoverflow_portugues.csv")

dados_ingles = pd.read_csv("data_sets/stackoverflow_ingles.csv")

dados_espanhol = pd.read_csv("data_sets/stackoverflow_espanhol.csv")

print("DATA PORTUGUESE")
display(dados_portugues.head()) 

print("DATA INGLES")
display(dados_ingles.head())

print("DATA ESPANHOL")
display(dados_espanhol.head())