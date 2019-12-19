import pandas as pd
import numpy as np

# 
dados_medicos = pd.read_csv("Dados-medicos.csv", sep=",", names=['idade', 'peso', 'carga_final', 'vo2_max'], skiprows=1)
dados_medicos = np.array(dados_medicos).astype(np.float)

coluna_idade = list(dados_medicos[:, 0])
coluna_peso = list(dados_medicos[:, 1])
coluna_carga_final = list(dados_medicos[:, 2])
coluna_vo2_max = list(dados_medicos[:, 3])

print("Estatísticas Idade")
print("\tMédia:", np.mean(coluna_idade))
print("\tVariância:", np.var(coluna_idade))
print("\tDesvio Padrão:", np.std(coluna_idade))

print("Estatísticas Peso")
print("\tMédia:", np.mean(coluna_peso))
print("\tVariância:", np.var(coluna_peso))
print("\tDesvio Padrão:", np.std(coluna_peso))

print("Estatísticas Carga Final")
print("\tMédia:", np.mean(coluna_carga_final))
print("\tVariância:", np.var(coluna_carga_final))
print("\tDesvio Padrão:", np.std(coluna_carga_final))

print("Estatísticas VO2 Max")
print("\tMédia:", np.mean(coluna_vo2_max))
print("\tVariância:", np.var(coluna_vo2_max))
print("\tDesvio Padrão:", np.std(coluna_vo2_max))
