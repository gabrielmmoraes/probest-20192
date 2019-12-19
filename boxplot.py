import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_medicos = pd.read_csv("Dados-medicos.csv", sep=",", skiprows=1)
dados_medicos = np.array(dados_medicos).astype(np.float)

coluna_idade = list(dados_medicos[:, 0])
coluna_peso = list(dados_medicos[:, 1])
coluna_carga_final = list(dados_medicos[:, 2])
coluna_vo2_max = list(dados_medicos[:, 3])

coluna = input("Escolha o dado a ser plotado (Idade = 1, Peso = 2, Carga Final = 3, VO2 Máximo = 4)\n")

if (coluna == '1'):
    # BoxPlot Idade
    plt.boxplot(coluna_idade)
    plt.title('BoxPlot Idade')
    plt.show()

elif (coluna == '2'):
    # BoxPlot Peso
    plt.boxplot(coluna_peso)
    plt.title('BoxPlot Peso')
    plt.show()

elif (coluna == '3'): 
    # BoxPlot Carga Final
    plt.boxplot(coluna_carga_final)
    plt.title('BoxPlot Carga Final')
    plt.show()

elif (coluna == '4'):
    # BoxPlot VO2 Máximo
    plt.boxplot(coluna_vo2_max)
    plt.title('BoxPlot VO2 Máximo')
    plt.show()

else:
    print("Selecione uma coluna de 1 a 4")