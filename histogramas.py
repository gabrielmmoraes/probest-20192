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
    # Histograma Idade
    bin_value = 3.49*np.std(coluna_idade)*1172**(-1/3)
    arr_bins = [i for i in np.arange(np.amin(coluna_idade),np.amax(coluna_idade)+bin_value, bin_value)]
    plt.hist(coluna_idade, bins=arr_bins)
    plt.title('Histograma Idade')
    plt.xlabel('Idade')
    plt.ylabel('Freq')
    plt.show()

elif (coluna == '2'):
    # Histograma Peso
    bin_value = 3.49*np.std(coluna_peso)*1172**(-1/3)
    arr_bins = [i for i in np.arange(np.amin(coluna_peso),np.amax(coluna_peso)+bin_value, bin_value)]
    plt.hist(coluna_peso, bins=arr_bins)
    plt.title('Histograma Peso')
    plt.xlabel('Peso')
    plt.ylabel('Freq')
    plt.show()

elif (coluna == '3'): 
    # Histograma Carga Final
    bin_value = 3.49*np.std(coluna_carga_final)*1172**(-1/3)
    arr_bins = [i for i in np.arange(np.amin(coluna_carga_final),np.amax(coluna_carga_final)+bin_value, bin_value)]
    plt.hist(coluna_carga_final, bins=arr_bins)
    plt.title('Histograma Carga Final')
    plt.xlabel('Carga Final')
    plt.ylabel('Freq')
    plt.show()

elif (coluna == '4'):
    # Histograma VO2 Máximo
    bin_value = 3.49*np.std(coluna_vo2_max)*1172**(-1/3)
    arr_bins = [i for i in np.arange(np.amin(coluna_vo2_max),np.amax(coluna_vo2_max)+bin_value, bin_value)]
    plt.hist(coluna_vo2_max, bins=arr_bins)
    plt.title('Histograma VO2 Máximo')
    plt.xlabel('VO2 Máximo')
    plt.ylabel('Freq')
    plt.show()

else:
    print("Selecione uma coluna de 1 a 4")

