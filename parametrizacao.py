import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

dados_medicos = pd.read_csv("Dados-medicos.csv", sep=",", skiprows=1)
dados_medicos = np.array(dados_medicos).astype(np.float)

coluna_idade = list(dados_medicos[:, 0])
coluna_peso = list(dados_medicos[:, 1])
coluna_carga_final = list(dados_medicos[:, 2])
coluna_vo2_max = list(dados_medicos[:, 3])

coluna = input("Escolha o dado a ser plotado (Idade = 1, Peso = 2, Carga Final = 3, VO2 Máximo = 4)\n")

if (coluna == '1'):
    # Parametrização Idade

    intervalo_dados = np.linspace(np.min(coluna_idade),np.max(coluna_idade)) 

    # Exponencial
    lambda_exponencial = 1/np.mean(coluna_idade)
    dist_exponencial = lambda_exponencial* np.exp(-(lambda_exponencial*intervalo_dados))
    plt.plot(intervalo_dados, dist_exponencial, label ="Exponencial")

    # Gaussiana
    estimativa_media_gaussiana = np.mean(coluna_idade)
    estimativa_variancia_gaussiana = np.var(coluna_idade)
    dist_gaussiana =(1/(np.sqrt(2*np.pi*estimativa_variancia_gaussiana)))* np.exp((-1/2)*((intervalo_dados-estimativa_media_gaussiana)**2)/estimativa_variancia_gaussiana)
    plt.plot(intervalo_dados, dist_gaussiana, label="Gaussiana")
   
    
    # Lognormal
    estimativa_media_lognormal= np.sum(np.log(coluna_idade))/len(coluna_idade)
    estimativa_variancia_lognormal= np.sum((np.log(coluna_idade)-estimativa_media_lognormal)**2)/len(coluna_idade)
    dist_lognormal= (1/(np.sqrt(2*np.pi*estimativa_variancia_lognormal)*intervalo_dados))* np.exp((-1/2)*((np.log(intervalo_dados)-estimativa_media_lognormal)**2)/estimativa_variancia_lognormal)
    plt.plot(intervalo_dados, dist_lognormal, label="Lognormal")

    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_idade,floc=0)
    dist_weibull = stats.weibull_min.pdf(intervalo_dados,parametros_weibull[0],loc=parametros_weibull[1], scale=parametros_weibull[2])
    plt.plot(intervalo_dados, dist_weibull, label="Weibull")

    # Plot usando os dados
    sns.kdeplot(coluna_idade, label="Idade")
    plt.title("Idade")
    plt.xlabel("Idade")
    
    print("Estimativa Lambda da Exponencial: ", lambda_exponencial)
    print("Estimativa Média da Gaussiana: ", estimativa_media_gaussiana)
    print("Estimativa do Desvio Padrão da Gaussiana: ", estimativa_variancia_gaussiana)
    print("Estimativa da Constante da Weibull: ", parametros_weibull[0])
    print("loc da Distribuição Weibull: ", parametros_weibull[1])
    print("Escala da Distribuição Weibull: ", parametros_weibull[2])

    plt.legend()
    plt.show()

elif (coluna == '2'):
    # Parametrização Peso

    intervalo_dados = np.linspace(np.min(coluna_peso),np.max(coluna_peso)) 

    # Exponencial
    lambda_exponencial = 1/np.mean(coluna_peso)
    dist_exponencial = lambda_exponencial* np.exp(-(lambda_exponencial*intervalo_dados))
    plt.plot(intervalo_dados, dist_exponencial, label ="Exponencial")

    # Gaussiana
    estimativa_media_gaussiana = np.mean(coluna_peso)
    estimativa_variancia_gaussiana = np.var(coluna_peso)
    dist_gaussiana =(1/(np.sqrt(2*np.pi*estimativa_variancia_gaussiana)))* np.exp((-1/2)*((intervalo_dados-estimativa_media_gaussiana)**2)/estimativa_variancia_gaussiana)
    plt.plot(intervalo_dados, dist_gaussiana, label="Gaussiana")
   
    
    # Lognormal
    estimativa_media_lognormal= np.sum(np.log(coluna_peso))/len(coluna_peso)
    estimativa_variancia_lognormal= np.sum((np.log(coluna_peso)-estimativa_media_lognormal)**2)/len(coluna_peso)
    dist_lognormal= (1/(np.sqrt(2*np.pi*estimativa_variancia_lognormal)*intervalo_dados))* np.exp((-1/2)*((np.log(intervalo_dados)-estimativa_media_lognormal)**2)/estimativa_variancia_lognormal)
    plt.plot(intervalo_dados, dist_lognormal, label="Lognormal")

    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_peso,floc=0)
    dist_weibull = stats.weibull_min.pdf(intervalo_dados,parametros_weibull[0],loc=parametros_weibull[1], scale=parametros_weibull[2])
    plt.plot(intervalo_dados, dist_weibull, label="Weibull")

    # Plot usando os dados
    sns.kdeplot(coluna_peso, label="Peso")
    plt.title("Peso")
    plt.xlabel("Peso")
    
    print("Estimativa Lambda da Exponencial: ", lambda_exponencial)
    print("Estimativa Média da Gaussiana: ", estimativa_media_gaussiana)
    print("Estimativa do Desvio Padrão da Gaussiana: ", estimativa_variancia_gaussiana)
    print("Estimativa da Constante da Weibull: ", parametros_weibull[0])
    print("loc da Distribuição Weibull: ", parametros_weibull[1])
    print("Escala da Distribuição Weibull: ", parametros_weibull[2])

    plt.legend()
    plt.show()


elif (coluna == '3'): 
    # Parametrização Carga Final

    intervalo_dados = np.linspace(np.min(coluna_carga_final),np.max(coluna_carga_final)) 

    # Exponencial
    lambda_exponencial = 1/np.mean(coluna_carga_final)
    dist_exponencial = lambda_exponencial* np.exp(-(lambda_exponencial*intervalo_dados))
    plt.plot(intervalo_dados, dist_exponencial, label ="Exponencial")

    # Gaussiana
    estimativa_media_gaussiana = np.mean(coluna_carga_final)
    estimativa_variancia_gaussiana = np.var(coluna_carga_final)
    dist_gaussiana =(1/(np.sqrt(2*np.pi*estimativa_variancia_gaussiana)))* np.exp((-1/2)*((intervalo_dados-estimativa_media_gaussiana)**2)/estimativa_variancia_gaussiana)
    plt.plot(intervalo_dados, dist_gaussiana, label="Gaussiana")
   
    
    # Lognormal
    estimativa_media_lognormal= np.sum(np.log(coluna_carga_final))/len(coluna_carga_final)
    estimativa_variancia_lognormal= np.sum((np.log(coluna_carga_final)-estimativa_media_lognormal)**2)/len(coluna_carga_final)
    dist_lognormal= (1/(np.sqrt(2*np.pi*estimativa_variancia_lognormal)*intervalo_dados))* np.exp((-1/2)*((np.log(intervalo_dados)-estimativa_media_lognormal)**2)/estimativa_variancia_lognormal)
    plt.plot(intervalo_dados, dist_lognormal, label="Lognormal")

    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_carga_final,floc=0)
    dist_weibull = stats.weibull_min.pdf(intervalo_dados,parametros_weibull[0],loc=parametros_weibull[1], scale=parametros_weibull[2])
    plt.plot(intervalo_dados, dist_weibull, label="Weibull")

    # Plot usando os dados
    sns.kdeplot(coluna_carga_final, label="Carga Final")
    plt.title("Carga Final")
    plt.xlabel("Carga Final")
    
    print("Estimativa Lambda da Exponencial: ", lambda_exponencial)
    print("Estimativa Média da Gaussiana: ", estimativa_media_gaussiana)
    print("Estimativa do Desvio Padrão da Gaussiana: ", estimativa_variancia_gaussiana)
    print("Estimativa da Constante da Weibull: ", parametros_weibull[0])
    print("loc da Distribuição Weibull: ", parametros_weibull[1])
    print("Escala da Distribuição Weibull: ", parametros_weibull[2])

    plt.legend()
    plt.show()

elif (coluna == '4'):
    # Parametrização VO2 Máximo

    intervalo_dados = np.linspace(np.min(coluna_vo2_max),np.max(coluna_vo2_max)) 

    # Exponencial
    lambda_exponencial = 1/np.mean(coluna_vo2_max)
    dist_exponencial = lambda_exponencial* np.exp(-(lambda_exponencial*intervalo_dados))
    plt.plot(intervalo_dados, dist_exponencial, label ="Exponencial")

    # Gaussiana
    estimativa_media_gaussiana = np.mean(coluna_vo2_max)
    estimativa_variancia_gaussiana = np.var(coluna_vo2_max)
    dist_gaussiana =(1/(np.sqrt(2*np.pi*estimativa_variancia_gaussiana)))* np.exp((-1/2)*((intervalo_dados-estimativa_media_gaussiana)**2)/estimativa_variancia_gaussiana)
    plt.plot(intervalo_dados, dist_gaussiana, label="Gaussiana")
   
    
    # Lognormal
    estimativa_media_lognormal= np.sum(np.log(coluna_vo2_max))/len(coluna_vo2_max)
    estimativa_variancia_lognormal= np.sum((np.log(coluna_vo2_max)-estimativa_media_lognormal)**2)/len(coluna_vo2_max)
    dist_lognormal= (1/(np.sqrt(2*np.pi*estimativa_variancia_lognormal)*intervalo_dados))* np.exp((-1/2)*((np.log(intervalo_dados)-estimativa_media_lognormal)**2)/estimativa_variancia_lognormal)
    plt.plot(intervalo_dados, dist_lognormal, label="Lognormal")

    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_vo2_max,floc=0)
    dist_weibull = stats.weibull_min.pdf(intervalo_dados,parametros_weibull[0],loc=parametros_weibull[1], scale=parametros_weibull[2])
    plt.plot(intervalo_dados, dist_weibull, label="Weibull")

    # Plot usando os dados
    sns.kdeplot(coluna_vo2_max, label="VO2 Máximo")
    plt.title("VO2 Máximo")
    plt.xlabel("VO2 Máximo")
    
    print("Estimativa Lambda da Exponencial: ", lambda_exponencial)
    print("Estimativa Média da Gaussiana: ", estimativa_media_gaussiana)
    print("Estimativa do Desvio Padrão da Gaussiana: ", estimativa_variancia_gaussiana)
    print("Estimativa da Constante da Weibull: ", parametros_weibull[0])
    print("loc da Distribuição Weibull: ", parametros_weibull[1])
    print("Escala da Distribuição Weibull: ", parametros_weibull[2])

    plt.legend()
    plt.show()

else:
    print("Selecione uma coluna de 1 a 4")