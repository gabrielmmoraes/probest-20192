import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


dados_medicos = pd.read_csv("Dados-medicos.csv", sep=",", skiprows=1)
dados_medicos = np.array(dados_medicos).astype(np.float)

coluna_idade = list(dados_medicos[:, 0])
coluna_peso = list(dados_medicos[:, 1])
coluna_carga_final = list(dados_medicos[:, 2])
coluna_vo2_max = list(dados_medicos[:, 3])

coluna = input("Escolha o dado a ser plotado (Idade = 1, Peso = 2, Carga Final = 3, VO2 Máximo = 4)\n")

if (coluna == '1'):
    # Parâmetro Idade
    
    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_idade,floc=0)
    stats.probplot(coluna_idade, dist='expon',sparams=parametros_exponencial,plot=plt)
    plt.title('Exponencial e Idade')
    plt.ylabel("Idade")
    plt.show()
    
    # Gaussiana
    parametros_gaussiana = stats.norm.fit(coluna_idade)
    stats.probplot(coluna_idade, dist='norm', sparams=parametros_gaussiana,plot=plt)
    plt.title('Gaussiana e Idade')
    plt.ylabel("Idade")
    plt.show()
    
    # Lognormal
    parametros_lognormal = stats.lognorm.fit(coluna_idade, floc=0)
    stats.probplot(coluna_idade, dist='lognorm',sparams=parametros_lognormal,plot=plt)
    plt.title('Lognormal e Idade')
    plt.ylabel("Idade")
    plt.show()
    
    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_idade,floc=0)
    stats.probplot(coluna_idade, dist='weibull_min',sparams=parametros_weibull,plot=plt)
    plt.title('Weibull e Idade')
    plt.ylabel("Idade")
    plt.show()

elif (coluna == '2'):
    # Parâmetro Peso
    
    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_peso,floc=0)
    stats.probplot(coluna_peso, dist='expon',sparams=parametros_exponencial,plot=plt)
    plt.title('Exponencial e Peso')
    plt.ylabel("Peso")
    plt.show()
    
    # Gaussiana
    parametros_gaussiana = stats.norm.fit(coluna_peso)
    stats.probplot(coluna_peso, dist='norm', sparams=parametros_gaussiana,plot=plt)
    plt.title('Gaussiana e Peso')
    plt.ylabel("Peso")
    plt.show()
    
    # Lognormal
    parametros_lognormal = stats.lognorm.fit(coluna_peso, floc=0)
    stats.probplot(coluna_peso, dist='lognorm',sparams=parametros_lognormal,plot=plt)
    plt.title('Lognormal e Peso')
    plt.ylabel("Peso")
    plt.show()
    
    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_peso,floc=0)
    stats.probplot(coluna_peso, dist='weibull_min',sparams=parametros_weibull,plot=plt)
    plt.title('Weibull e Peso')
    plt.ylabel("Peso")
    plt.show()

elif (coluna == '3'):
    # Parâmetro Carga Final   
    
    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_carga_final,floc=0)
    stats.probplot(coluna_carga_final, dist='expon',sparams=parametros_exponencial,plot=plt)
    plt.title('Exponencial e Carga Final')
    plt.ylabel("Carga Final")
    plt.show()
    
    # Gaussiana
    parametros_gaussiana = stats.norm.fit(coluna_carga_final)
    stats.probplot(coluna_carga_final, dist='norm', sparams=parametros_gaussiana,plot=plt)
    plt.title('Gaussiana e Carga Final')
    plt.ylabel("Carga Final")
    plt.show()
    
    # Lognormal
    parametros_lognormal = stats.lognorm.fit(coluna_carga_final, floc=0)
    stats.probplot(coluna_carga_final, dist='lognorm',sparams=parametros_lognormal,plot=plt)
    plt.title('Lognormal e Carga Final')
    plt.ylabel("Carga Final")
    plt.show()
    
    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_carga_final,floc=0)
    stats.probplot(coluna_carga_final, dist='weibull_min',sparams=parametros_weibull,plot=plt)
    plt.title('Weibull e Carga Final')
    plt.ylabel("Carga Final")
    plt.show()

elif (coluna == '4'):
    # Parâmetro VO2 Máximo
    
    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_vo2_max,floc=0)
    stats.probplot(coluna_vo2_max, dist='expon',sparams=parametros_exponencial,plot=plt)
    plt.title('Exponencial e VO2 Máximo')
    plt.ylabel("VO2 Máximo")
    plt.show()
    
    # Gaussiana
    parametros_gaussiana = stats.norm.fit(coluna_vo2_max)
    stats.probplot(coluna_vo2_max, dist='norm', sparams=parametros_gaussiana,plot=plt)
    plt.title('Gaussiana e VO2 Máximo')
    plt.ylabel("VO2 Máximo")
    plt.show()
    
    # Lognormal
    parametros_lognormal = stats.lognorm.fit(coluna_vo2_max, floc=0)
    stats.probplot(coluna_vo2_max, dist='lognorm',sparams=parametros_lognormal,plot=plt)
    plt.title('Lognormal e VO2 Máximo')
    plt.ylabel("VO2 Máximo")
    plt.show()
    
    # Weibull
    parametros_weibull = stats.weibull_min.fit(coluna_vo2_max,floc=0)
    stats.probplot(coluna_vo2_max, dist='weibull_min',sparams=parametros_weibull,plot=plt)
    plt.title('Weibull e VO2 Máximo')
    plt.ylabel("VO2 Máximo")
    plt.show()

else:
    print("Selecione uma coluna de 1 a 4")
