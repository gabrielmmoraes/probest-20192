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

if (coluna == "1"):
    # Idade

    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_idade,floc=0)
    exponencial_KS = stats.kstest(coluna_idade, 'expon', parametros_exponencial)
    print("Distribuição Exponencial")
    print("D = ", exponencial_KS[0])
    print("p_valor = ", exponencial_KS[1], "\n")

    # Gaussiana
    print("Distribuição Gaussiana")
    parametros_gaussiana = stats.norm.fit(coluna_idade)
    gauss_KS = stats.kstest(coluna_idade, 'norm', parametros_gaussiana)
    print("D = ", gauss_KS[0])
    print("p_valor = ", gauss_KS[1], "\n")

    # Lognormal
    print("Distribuição Lognormal")
    parametros_lognormal = stats.lognorm.fit(coluna_idade, floc=0)
    lognormal_KS = stats.kstest(coluna_idade,'lognorm', parametros_lognormal)
    print("D = ", lognormal_KS[0])
    print("p_value = ", lognormal_KS[1], "\n")

    # Weibull
    print("Distribuição Weibull")
    parametros_weibull = stats.weibull_min.fit(coluna_idade,floc=0)
    weibull_KS = stats.kstest(coluna_idade, 'weibull_min', parametros_weibull)
    print("D = ", weibull_KS[0])
    print("p_value = ", weibull_KS[1])

elif (coluna == "2"):
    # Peso

    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_peso,floc=0)
    exponencial_KS = stats.kstest(coluna_peso, 'expon', parametros_exponencial)
    print("Distribuição Exponencial")
    print("D = ", exponencial_KS[0])
    print("p_valor = ", exponencial_KS[1], "\n")

    # Gaussiana
    print("Distribuição Gaussiana")
    parametros_gaussiana = stats.norm.fit(coluna_peso)
    gauss_KS = stats.kstest(coluna_peso, 'norm', parametros_gaussiana)
    print("D = ", gauss_KS[0])
    print("p_valor = ", gauss_KS[1], "\n")

    # Lognormal
    print("Distribuição Lognormal")
    parametros_lognormal = stats.lognorm.fit(coluna_peso, floc=0)
    lognormal_KS = stats.kstest(coluna_peso,'lognorm', parametros_lognormal)
    print("D = ", lognormal_KS[0])
    print("p_value = ", lognormal_KS[1], "\n")

    # Weibull
    print("Distribuição Weibull")
    parametros_weibull = stats.weibull_min.fit(coluna_peso,floc=0)
    weibull_KS = stats.kstest(coluna_peso, 'weibull_min', parametros_weibull)
    print("D = ", weibull_KS[0])
    print("p_value = ", weibull_KS[1])

elif (coluna == "3"):
    # Carga Final

    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_carga_final,floc=0)
    exponencial_KS = stats.kstest(coluna_carga_final, 'expon', parametros_exponencial)
    print("Distribuição Exponencial")
    print("D = ", exponencial_KS[0])
    print("p_valor = ", exponencial_KS[1], "\n")

    # Gaussiana
    print("Distribuição Gaussiana")
    parametros_gaussiana = stats.norm.fit(coluna_carga_final)
    gauss_KS = stats.kstest(coluna_carga_final, 'norm', parametros_gaussiana)
    print("D = ", gauss_KS[0])
    print("p_valor = ", gauss_KS[1], "\n")

    # Lognormal
    print("Distribuição Lognormal")
    parametros_lognormal = stats.lognorm.fit(coluna_carga_final, floc=0)
    lognormal_KS = stats.kstest(coluna_carga_final,'lognorm', parametros_lognormal)
    print("D = ", lognormal_KS[0])
    print("p_value = ", lognormal_KS[1], "\n")

    # Weibull
    print("Distribuição Weibull")
    parametros_weibull = stats.weibull_min.fit(coluna_carga_final,floc=0)
    weibull_KS = stats.kstest(coluna_carga_final, 'weibull_min', parametros_weibull)
    print("D = ", weibull_KS[0])
    print("p_value = ", weibull_KS[1])

elif (coluna == "4"):
    #VO2 Máximo

    # Exponencial
    parametros_exponencial = stats.expon.fit(coluna_vo2_max,floc=0)
    exponencial_KS = stats.kstest(coluna_vo2_max, 'expon', parametros_exponencial)
    print("Distribuição Exponencial")
    print("D = ", exponencial_KS[0])
    print("p_valor = ", exponencial_KS[1], "\n")

    # Gaussiana
    print("Distribuição Gaussiana")
    parametros_gaussiana = stats.norm.fit(coluna_vo2_max)
    gauss_KS = stats.kstest(coluna_vo2_max, 'norm', parametros_gaussiana)
    print("D = ", gauss_KS[0])
    print("p_valor = ", gauss_KS[1], "\n")

    # Lognormal
    print("Distribuição Lognormal")
    parametros_lognormal = stats.lognorm.fit(coluna_vo2_max, floc=0)
    lognormal_KS = stats.kstest(coluna_vo2_max,'lognorm', parametros_lognormal)
    print("D = ", lognormal_KS[0])
    print("p_value = ", lognormal_KS[1], "\n")

    # Weibull
    print("Distribuição Weibull")
    parametros_weibull = stats.weibull_min.fit(coluna_vo2_max,floc=0)
    weibull_KS = stats.kstest(coluna_vo2_max, 'weibull_min', parametros_weibull)
    print("D = ", weibull_KS[0])
    print("p_value = ", weibull_KS[1])
