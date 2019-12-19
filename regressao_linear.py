import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dados_medicos = pd.read_csv("Dados-medicos.csv", sep=",", skiprows=1)
dados_medicos = np.array(dados_medicos).astype(np.float)

coluna_idade = list(dados_medicos[:, 0])
coluna_peso = list(dados_medicos[:, 1])
coluna_carga_final = list(dados_medicos[:, 2])
coluna_vo2_max = list(dados_medicos[:, 3])

coluna = input("Escolha o dado a ser plotado (Idade = 1, Peso = 2, Carga Final = 3)\n")

if (coluna == '1'):
    # Idade e VO2 Máximo

    coeficiente_correlacao = (np.sum((coluna_peso - np.mean(coluna_peso)) * (coluna_vo2_max - np.mean(coluna_vo2_max)))) / (np.sqrt(np.sum((coluna_peso - np.mean(coluna_peso))**2)) * np.sqrt(np.sum((coluna_vo2_max - np.mean(coluna_vo2_max))**2)))    
    
    a = np.arange(np.min(coluna_idade), np.max(coluna_idade))
    regressao_linear = np.polyfit(coluna_idade, coluna_vo2_max, 1)
    
    plt.title('Scatterplot da Idade e VO2 máximo')
    sns.scatterplot(x = coluna_idade, y = coluna_vo2_max, color = "Blue")    
    plt.plot(a, regressao_linear[1] + regressao_linear[0] * a, '--', color="Black")
    plt.show()

    print("Coeficiente de correlação entre Idade e VO2 máximo: ", coeficiente_correlacao)
    print("Regressão linear: ", regressao_linear)

elif (coluna == '2'):
    # Peso e VO2 Máximo

    coeficiente_correlacao = (np.sum((coluna_peso - np.mean(coluna_peso)) * (coluna_vo2_max - np.mean(coluna_vo2_max)))) / (np.sqrt(np.sum((coluna_peso - np.mean(coluna_peso))**2)) * np.sqrt(np.sum((coluna_vo2_max - np.mean(coluna_vo2_max))**2)))

    a = np.arange(np.min(coluna_peso), np.max(coluna_peso))
    regressao_linear = np.polyfit(coluna_peso, coluna_vo2_max, 1)
    
    plt.title('Scatterplot do Peso e VO2 máximo')
    sns.scatterplot(x = coluna_peso, y = coluna_vo2_max, color = "Red")    
    plt.plot(a, regressao_linear[1] + regressao_linear[0] * a, '--', color="Black")
    plt.show()

    print("Coeficiente de correlação entre Idade e VO2 máximo: ", coeficiente_correlacao)
    print("Regressão linear: ", regressao_linear)

elif (coluna == '3'): 
    # Carga Final e VO2 Máximo

    coeficiente_correlacao = (np.sum((coluna_peso - np.mean(coluna_peso)) * (coluna_vo2_max - np.mean(coluna_vo2_max)))) / (np.sqrt(np.sum((coluna_peso - np.mean(coluna_peso))**2)) * np.sqrt(np.sum((coluna_vo2_max - np.mean(coluna_vo2_max))**2)))        

    a = np.arange(np.min(coluna_carga_final), np.max(coluna_carga_final))
    regressao_linear = np.polyfit(coluna_carga_final, coluna_vo2_max, 1)
    
    plt.title('Scatterplot da Carga Final e VO2 máximo')
    sns.scatterplot(x = coluna_carga_final, y = coluna_vo2_max, color = "Green")    
    plt.plot(a, regressao_linear[1] + regressao_linear[0] * a, '--', color="Black")
    plt.show()

    print("Coeficiente de correlação entre Idade e VO2 máximo: ", coeficiente_correlacao)
    print("Regressão linear: ", regressao_linear)

else:
    print("Selecione uma coluna de 1 a 3")

