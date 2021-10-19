#!/usr/bin/env python
# coding: utf-8

# In[118]:


#Carregar bibliotecas gerais
import pandas as pd
import numpy as np
import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import locale
import warnings
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf
get_ipython().system('pip install pmdarima')
from pmdarima.arima import auto_arima


# In[119]:


#Lendo os arquivos
acidente = pd.read_excel(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Final\ACID_RJ_FIN.xlsx", squeeze=True)
infracao = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Final\INFRA_RJ_FIN.csv", sep = ',')


# # ##########################################################
# #  .................................. BASE ACIDENTES...............................................
# #  ##########################################################

# In[120]:


import copy
acidente_copy = pd.DataFrame(columns = acidente.columns, data = copy.deepcopy(acidente.values))
acidente1 = acidente_copy.astype({"Data":str})
acidente1.info()


# In[121]:


# Verificando
acidente1.info()


# In[122]:


acidente1.head(1)


# In[123]:


acidente1.set_index('mes_ano',inplace = True)
acidente1.head()


# ## Criando as séries - Acidentes

# In[124]:


#Criando a serie de Ocorrências por ano
acid_porano = acidente1.groupby('ano').size()
acid_porano.head()


# In[125]:


#Criando a serie de Ocorrências por ano
acid_pormes = acidente1.groupby('Mes').size().sort_values(ascending=False)
acid_pormes


# In[126]:


#Criando a serie de Ocorrências por mes_ano
acid_mesano = acidente1.groupby('mes_ano').size()
acid_mesano.head()


# In[127]:


acid_ano_periodo = acidente1.groupby(['ano','Periodo']).agg({'Periodo': 'count'}).unstack()
acid_ano_periodo.head()


# In[128]:


acid_ano_mes = acidente1.groupby(['ano','Mes']).agg({'Mes': 'count'}).unstack()
acid_ano_mes.head()


# In[129]:


acid_mesporano = acidente1.groupby(['Mes','ano']).agg({'ano': 'count'}).unstack()
acid_mesporano


# In[130]:


acid_ano_br = acidente1.groupby(['ano','BR']).agg({'BR': 'count'}).unstack()
acid_ano_br.head()


# ## Plotando os gráficos  - Acidentes

# In[131]:


#Plotando gráfico "Acidentes por Mês/Ano no Rio de Janeiro'
ax = acid_mesano.plot(kind='line', color = 'red', title='Acidentes por Mês/Ano no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Mês/Ano')
plt.show()


# In[132]:


#Plotando gráfico "Acidentes por Mês no Rio de Janeiro'
ax = acid_pormes.plot(kind='bar', color = 'red', title='Acidentes por Mês no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Mês')
plt.show()


# In[133]:


# Plotando gráfico "Acidentes por Ano no Rio de Janeiro'
ax = acid_porano.plot(kind='bar', color = 'red', title='Total de acidentes por Ano no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Ano')
plt.show()


# In[134]:


# Plotando gráfico "Acidentes por Período por Ano no Rio de Janeiro'
ax = acid_ano_periodo.plot(kind='bar', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Ano')
ax.set_title('Acidentes por Período por Ano no Rio de Janeiro', fontsize = 20)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})
plt.show()


# In[135]:


# Plotando gráfico "Acidentes por Ano por período no Rio de Janeiro'
ax = acid_ano_mes.plot(kind='bar', title='Acidentes por MÊs em Ano  por Período no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Ano')
ax.set_title('Acidentes por Mês em Ano no Rio de Janeiro', fontsize = 20)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})
plt.show()


# In[136]:


# Plotando gráfico "Acidentes por Mês e por Ano no Rio de Janeiro'
ax = acid_mesporano.plot(kind='bar', title='Acidentes por Mês e Ano no Rio de Janeiro', figsize=(15,8))

ax.set_ylabel('Acidentes', fontsize = 15)
ax.set_xlabel('Ano', fontsize = 15)
ax.set_title('Acidentes por Mês e Ano no Rio de Janeiro', fontsize=22)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})

plt.show()


# In[137]:


# Plotando gráfico "Acidentes por Mês e por Ano no Rio de Janeiro' - linha
ax = acid_mesporano.plot(kind='line', title='Acidentes por Mês e Ano no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Ano')
plt.show()


# In[138]:


# Plotando gráfico "Acidentes por BR por Ano no Rio de Janeiro'
ax = acid_ano_br.plot(kind='bar', figsize=(15,8))
ax.set_title('Acidentes por BR por Ano no Rio de Janeiro', fontsize=22)
ax.set_ylabel('Acidentes', fontsize=15)
ax.set_xlabel('Ano', fontsize=17)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})
plt.show()


# In[139]:


# Plotando gráfico boxplot com os quartis, outliers, valores mínimos e máximos
acid_mesano.plot.box(figsize=(15,8), grid = True)
plt.rcParams.update({'font.size': 15})


# ## Dados estatísticos das Séries - Acidentes

# In[140]:


# Análise estatística dos acidentes por Mês-ano
acid_mesano.describe()


# In[141]:


# Análise estatística dos acidentes por ano
acid_porano.describe()


# ## Retirando Outliers - Acidentes

# In[142]:


# Analisando MÊs-Ano
#Determinando os qs
q1= 1332
q2 = 1465.5
q3= 1654.75
iqr = (q3-q1)
fator = 1.5
lowpass = q1-(iqr*fator)
highpass = q3+(iqr*fator)

def removeoutlier(value):
        if value > highpass: 
            return -1
        elif value < lowpass:
            return -1
        else:
            return value


# In[143]:


acidente2 = acid_mesano.apply(lambda value: removeoutlier(value))


# In[144]:


acidente2.sort_values(ascending=True)[:3]


# In[145]:


acidente_ok = acidente2.drop(labels = ['2020-12', '2020-09'])
acidente_ok.sort_values(ascending=True)[:5]


# In[146]:


# Plotando gráfico boxplot com os quartis, outliers, valores mínimos e máximos
acidente_ok.plot.box(figsize=(15,8), grid = True)


# # ---------------------------------------------------------------------------------------------------------------
# # Iniciar preparação para o ARIMA  - Acidentes
# # ---------------------------------------------------------------------------------------------------------------

# ## Dividindo as bases
# 
# Total são 46 meses (pois retiramos 2 de 2020)
# 
# BASE DE TREINO -> Então ficam 80% de 46 = 36.8 que vamos aproximar para 37
# 
# BASE DE TESTE -> Os últimos 9 meses

# In[147]:


import copy
prebases = acidente_ok.copy(deep=True)
type(prebases)


# In[148]:


# Criando e visualizando base treino
acid_treino = prebases.iloc[0:37]
acid_treino


# In[149]:


type(acid_treino)


# In[150]:


acid_treino.shape


# In[151]:


# Criando e visualizando base teste
acid_teste = prebases.iloc[37:47]
acid_teste


# In[152]:


type(acid_teste)


# In[153]:


acid_teste.shape


# ## Processo de escolha de Parâmetros - Acidentes

# In[154]:


# Primeiro vamos decompor a amostra para entender tendência, sazonalidade e resíduo
decomposicao = seasonal_decompose(acid_treino, period=12)
imagem = decomposicao.plot()


# In[155]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo

fig, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao.trend.plot(ax=ax1, title='Análise de Acidentes no Rio de Janeiro por Mês/Ano')
ax1.set_ylabel('Tendência')

decomposicao.resid.plot(ax=ax2)
ax2.set_ylabel('Resíduo')

decomposicao.seasonal.plot(ax=ax3)
ax3.set_ylabel('Sazonalidade')


# In[156]:


#Autocorrelação (AR)
acid_autocor = sm.graphics.tsa.plot_acf(acid_treino.values.squeeze(),lags = 15)


# In[157]:


#Média móvel (MA)
sm.graphics.tsa.plot_pacf(acid_treino.values.squeeze(), lags = 15)


# ## Vamos aplicar o teste de Dickey Fuller para descobrir se a série é estacionária

# In[158]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller
xx = acid_treino.values
result = adfuller(xx)
print('ADF Statistic: %f' % result[0])
print('p-value:%f'% result[1])
print('Num de observações usadas para regressão ADF %f'% result [3])
print("Critical Values:")
for key, values in result[4].items():
    print('\t%s: %.3f' % (key, values))

# O p-value deu bem pequeno (<0,05%), então consideramos a série como estacionária.


# # .................................................................................................................................
# # MODELO AUTO ARIMA - ACIDENTES
# # .................................................................................................................................

# #  Auto ARIMA - Acidentes

# In[245]:


# Criando o modelo do auto arima
autoarima_acid = auto_arima(acid_treino, trace=True, seasonal = True, start_p = 0, start_q =0, max_p = 2, max_q = 2, d=0, error_action='ignore', suppress_warnings=True, stepwise=True)
autoarima_acid_ajustado = autoarima_acid.fit(acid_treino)
autoarima_acid_ajustado


# In[247]:


# Sumário do modelo
autoarima_acid_ajustado.summary()


# In[161]:


# Criando o Forecast
forecast_autoarima_acid = autoarima_acid.predict(n_periods=len(acid_teste))
forecast_autoarima_acid = pd.DataFrame(forecast_autoarima_acid,index = acid_teste.index,columns=['Prediction'])


# In[162]:


# Reindexando Base Teste
newindexteste = ['2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-10', '2020-11']
acid_teste.reindex(newindexteste)
acid_teste


# In[163]:


# Reindexando Base Treino
newindextreino = ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01']
acid_treino.reindex(newindextreino)
acid_treino


# In[244]:


# Plotando a comparação Predições x Esperado
plt.figure(figsize = (16,8))
plt.plot(acid_treino, label='Acidentes base treino')
plt.plot(acid_teste, label='Acidentes base teste')
plt.plot(forecast_autoarima_acid, label='Predição')
plt.title("Modelo ARIMA -- Acidentes", fontsize=20)
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.legend()
plt.rcParams.update({'font.size': 9})
plt.show()


# In[241]:


# Focando no período predito
plt.figure(figsize = (16,8))
plt.plot(acid_teste, label='Acidentes base teste', color = 'orange')
plt.plot(forecast_autoarima_acid, label='Predição', color = 'green')
plt.title("Modelo ARIMA -- Acidentes", fontsize=20)
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.show()


# # ##########################################################
# # ##########################################################
# #  .................................. BASE INFRAÇÕES...............................................
# #  ##########################################################
# # ##########################################################

# In[166]:


import copy
infracao_copy = pd.DataFrame(columns = infracao.columns, data = copy.deepcopy(infracao.values))
infracao1 = infracao_copy.astype({"Data":str})
infracao1.info()


# In[167]:


# Verificando os tipos das colunas
infracao1.info()


# In[168]:


#Convertendo tipos de colunas
infracao1['Data']= pd.to_datetime(infracao1['Data'])
infracao1.head()


# In[169]:


infracao1.set_index('mes_ano',inplace = True)


# ## Criando as séries - Infrações

# In[170]:


#Criando a serie de Ocorrências por ano
infra_porano = infracao1.groupby('ano').size()
infra_porano.head()


# In[171]:


#Criando a série de Ocorrências por ano
infra_pormes = infracao1.groupby('Mes').size().sort_values(ascending=False)
infra_pormes


# In[172]:


#Criando a serie de Ocorrências por mes_ano
infra_mesano = infracao1.groupby('mes_ano').size()
infra_mesano.head()


# In[173]:


infra_mesporano = infracao1.groupby(['Mes','ano']).agg({'ano': 'count'}).unstack()
infra_mesporano


# In[174]:


infra_ano_periodo = infracao1.groupby(['ano','Periodo']).agg({'Periodo': 'count'}).unstack()
infra_ano_periodo


# In[175]:


infra_ano_tipo = infracao1.groupby(['ano','Tipo']).agg({'Tipo': 'count'}).unstack()
infra_ano_tipo


# In[176]:


infra_mesano_tipo = infracao1.groupby(['Mes', 'Tipo']).agg({'Tipo': 'count'}).unstack()
infra_mesano_tipo


# In[177]:


infra_ano_br = infracao1.groupby(['ano','BR']).agg({'BR': 'count'}).unstack()
infra_ano_br.head()


# ## Plotando os gráficos - Infrações

# In[178]:


#Plotando gráfico "Infrações por Mês/Ano no Rio de Janeiro'
ax = infra_mesano.plot(kind='line', color = 'orange', title='Infrações por Mês/Ano no Rio de Janeiro', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Mês/Ano')
plt.rcParams.update({'font.size': 15})

plt.show()


# In[179]:


#Plotando gráfico "Infrações por Mês no Rio de Janeiro'
ax = infra_pormes.plot(kind='bar', color = 'orange', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Mês no Rio de Janeiro', fontsize = 20)
plt.rcParams.update({'font.size': 15})

plt.show()


# In[180]:


#Plotando gráfico "Infrações por Ano no Rio de Janeiro'
ax = infra_porano.plot(kind='bar', color = 'orange', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Ano no Rio de Janeiro', fontsize = 20)
plt.rcParams.update({'font.size': 15})

plt.show()


# In[181]:


#Plotando gráfico "Infrações por Mês e por Ano no Rio de Janeiro'
ax = infra_mesporano.plot(kind='bar', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Mes por Ano no Rio de Janeiro', fontsize = 20)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})

plt.show()


# In[182]:


#Plotando gráfico "Infrações por Mês e por Ano no Rio de Janeiro'
ax = infra_mesporano.plot(kind='line', figsize=(15,8))
ax.set_ylabel('Acidentes')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Mes por Ano no Rio de Janeiro', fontsize = 20)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})

plt.show()


# In[183]:


#Plotando gráfico "Infrações por Período e Ano no Rio de Janeiro'
ax = infra_ano_periodo.plot(kind='bar', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')

ax.set_title('Infrações por Período por Ano no Rio de Janeiro', fontsize = 20)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})

plt.show()


# In[184]:


#Plotando gráfico "Infrações por Tipo Ano no Rio de Janeiro'
ax = infra_ano_tipo.plot(kind='bar',  figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Tipo por Ano no Rio de Janeiro', fontsize = 20)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})
plt.show()


# In[185]:


#Plotando gráfico "Infrações por Tipo Ano no Rio de Janeiro'
ax = infra_mesano_tipo.plot(kind='bar',  figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('Ano')
ax.set_title('Infrações por Tipo por Mês no Rio de Janeiro', fontsize = 20)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 15})
plt.show()


# In[186]:


#Plotando gráfico "Infrações por BR no Rio de Janeiro'
ax = infra_ano_br.plot(kind='bar', figsize=(15,8))
ax.set_ylabel('Infrações')
ax.set_xlabel('BR')
ax.set_title('Infrações por BR no Rio de Janeiro', fontsize = 20)
plt.rcParams.update({'font.size': 15})

plt.show()


# In[187]:


# Plotando gráfico boxplot com os quartis, outliers, valores mínimos e máximos
infra_mesano.plot.box(figsize=(15,8), grid = True)


# ## Dados estatísticos das Séries - Infrações

# In[188]:


# Análise estatística de Infrações por Mês-Ano
infra_mesano.describe()


# In[189]:


# Análise estatística de Infrações por Ano
infra_porano.describe()


# ## Retirando Outliers - Infrações

# In[190]:


#Determinando os qs (infra_mesano)
novo_q1= 63754.25
novo_q2 = 78141
novo_q3= 91767.25
iqr = (novo_q3-novo_q1)
fator = 1.5
lowpass = novo_q1-(iqr*fator)
highpass = novo_q3+(iqr*fator)


def removeoutlier1(value):
        if value > highpass: 
            return -1
        elif value < lowpass:
            return -1
        else:
            return value


# In[191]:


infracao3 = infra_mesano.apply(lambda value: removeoutlier1(value))


# In[192]:


infracao3.sort_values(ascending=True)[:5]


# In[193]:


infracao_ok = infracao3.drop(labels = ['2017-07'])
infracao_ok.sort_values(ascending=True)[:5]


# In[194]:


# Plotando gráfico boxplot com os quartis, outliers, valores mínimos e máximos
infracao_ok.plot.box(figsize=(15,8), grid = True)


# # Iniciar preparaçao para o ARIMA - Infrações

# ## Dividindo as bases
# Total são 47 meses (pois retiramos 1 de 2017)
# 
# BASE DE TREINO -> Então ficam 80% de 47 = 37.6 que vamos aproximar para 38
# 
# BASE DE TESTE -> Os últimos 9 meses

# In[195]:


import copy
prebases1 = infracao_ok.copy(deep=True)
type(prebases1)


# In[196]:


# Criando e visualizando base treino
infra_treino = prebases1.iloc[0:38]
infra_treino


# In[197]:


type(infra_treino)


# In[198]:


infra_treino.shape


# In[199]:


# Criando e visualizando base teste
infra_teste = prebases1.iloc[38:47]
infra_teste


# In[200]:


type(infra_teste)


# In[201]:


infra_teste.shape


# ## Análises Estatísticas - Infrações

# In[202]:


# Primeiro vamos decompor a amosta para entender tendência, sazonalidade e resíduo
decomposicao2 = seasonal_decompose(infra_treino, period=12)
imagem2 = decomposicao.plot()


# In[203]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo_fig, (novo_ax1,novo_ax2,novo_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao2.trend.plot(ax= novo_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo_ax1.set_ylabel('Tendência')

decomposicao2.resid.plot(ax= novo_ax2)
novo_ax2.set_ylabel('Resíduo')

decomposicao2.seasonal.plot(ax = novo_ax3)
novo_ax3.set_ylabel('Sazonalidade')


# In[204]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller
az = infra_treino.values
result2 = adfuller(az)
print('ADF Statistic: %f' % result2[0])
print('p-value:%f'% result2[1])
print("Critical Values:")
for key, values in result2[4].items():
    print('\t%s: %.3f' % (key, values))

# O p-value foi > 0,05%, então consideramos a série como não estacionária.


# In[88]:


# Aplicando a diferenciação na série e removendo dados nulos
infra_treino_diff1 = infra_treino.diff()
infra_treino_diff1 = infra_treino_diff1.dropna()


# In[303]:


# Decompondo os dado agora da série diferenciada
decomposicao3 = seasonal_decompose(infra_treino_diff1, period=12)
imagem3 = decomposicao3.plot()


# In[304]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo2_fig, (novo2_ax1,novo2_ax2,novo2_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao3.trend.plot(ax= novo2_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo2_ax1.set_ylabel('Tendência')

decomposicao3.resid.plot(ax= novo2_ax2)
novo2_ax2.set_ylabel('Resíduo')

decomposicao3.seasonal.plot(ax = novo2_ax3)
novo2_ax3.set_ylabel('Sazonalidade')


# In[315]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller

az2 = infra_treino_diff1.values
result3 = adfuller(az2)
print('ADF Statistic: %f' % result3[0])
print('p-value:%f'% result3[1])
print("Critical Values:")
for key, values in result3[4].items():
    print('\t%s: %.3f' % (key, values))


# In[307]:


# Aplicando a diferenciação na série e removendo dados nulos
infra_treino_diff2 = infra_treino_diff1.diff()
infra_treino_diff2 = infra_treino_diff2.dropna()


# In[308]:


# Decompondo os dado agora da série diferenciada
decomposicao4 = seasonal_decompose(infra_treino_diff2, period=12)
imagem4 = decomposicao4.plot()


# In[309]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo3_fig, (novo3_ax1,novo3_ax2,novo3_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao4.trend.plot(ax= novo3_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo3_ax1.set_ylabel('Tendência')

decomposicao4.resid.plot(ax= novo3_ax2)
novo3_ax2.set_ylabel('Resíduo')

decomposicao4.seasonal.plot(ax = novo3_ax3)
novo3_ax3.set_ylabel('Sazonalidade')


# In[316]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller

az3 = infra_treino_diff2.values
result4 = adfuller(az3)
print('ADF Statistic: %f' % result4[0])
print('p-value:%f'% result4[1])
print("Critical Values:")
for key, values in result4[4].items():
    print('\t%s: %.3f' % (key, values))


# In[311]:


# Aplicando a diferenciação na série e removendo dados nulos
infra_treino_diff3 = infra_treino_diff2.diff()
infra_treino_diff3 = infra_treino_diff3.dropna()


# In[312]:


# Decompondo os dado agora da série diferenciada
decomposicao5 = seasonal_decompose(infra_treino_diff3, period=12)
imagem5 = decomposicao5.plot()


# In[313]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo4_fig, (novo4_ax1,novo4_ax2,novo4_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao5.trend.plot(ax= novo4_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo4_ax1.set_ylabel('Tendência')

decomposicao5.resid.plot(ax= novo4_ax2)
novo4_ax2.set_ylabel('Resíduo')

decomposicao5.seasonal.plot(ax = novo4_ax3)
novo4_ax3.set_ylabel('Sazonalidade')


# In[317]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller

az4 = infra_treino_diff3.values
result5 = adfuller(az4)
print('ADF Statistic: %f' % result5[0])
print('p-value:%f'% result5[1])
print("Critical Values:")
for key, values in result5[4].items():
    print('\t%s: %.3f' % (key, values))


# In[318]:


# Aplicando a diferenciação na série e removendo dados nulos
infra_treino_diff4 = infra_treino_diff3.diff()
infra_treino_diff4 = infra_treino_diff4.dropna()


# In[319]:


# Decompondo os dado agora da série diferenciada
decomposicao6 = seasonal_decompose(infra_treino_diff4, period=12)
imagem6 = decomposicao6.plot()


# In[320]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo5_fig, (novo5_ax1,novo5_ax2,novo5_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao6.trend.plot(ax= novo5_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo5_ax1.set_ylabel('Tendência')

decomposicao6.resid.plot(ax= novo5_ax2)
novo5_ax2.set_ylabel('Resíduo')

decomposicao6.seasonal.plot(ax = novo5_ax3)
novo5_ax3.set_ylabel('Sazonalidade')


# In[321]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller

az5 = infra_treino_diff4.values
result6 = adfuller(az5)
print('ADF Statistic: %f' % result6[0])
print('p-value:%f'% result6[1])
print("Critical Values:")
for key, values in result6[4].items():
    print('\t%s: %.3f' % (key, values))


# In[322]:


# Aplicando a diferenciação na série e removendo dados nulos
infra_treino_diff5 = infra_treino_diff4.diff()
infra_treino_diff5 = infra_treino_diff5.dropna()


# In[323]:


# Decompondo os dado agora da série diferenciada
decomposicao7 = seasonal_decompose(infra_treino_diff5, period=12)
imagem7 = decomposicao7.plot()


# In[324]:


# Vamos decompor a amostra para entender tendência, sazonalidade e resíduo
novo6_fig, (novo6_ax1,novo6_ax2,novo6_ax3) = plt.subplots(3,1, figsize=(15,8))

decomposicao7.trend.plot(ax= novo6_ax1, title='Análise de Infrações no Rio de Janeiro por Mês/Ano')
novo5_ax1.set_ylabel('Tendência')

decomposicao7.resid.plot(ax= novo6_ax2)
novo6_ax2.set_ylabel('Resíduo')

decomposicao7.seasonal.plot(ax = novo6_ax3)
novo6_ax3.set_ylabel('Sazonalidade')


# In[325]:


# Teste Dickey-Fuller - função para exibir o teste Augmented Dickey-Fuller

az6 = infra_treino_diff5.values
result7 = adfuller(az6)
print('ADF Statistic: %f' % result7[0])
print('p-value:%f'% result7[1])
print("Critical Values:")
for key, values in result7[4].items():
    print('\t%s: %.3f' % (key, values))


# In[205]:


#Autocorrelação (AR)
infra_autocor = sm.graphics.tsa.plot_acf(infra_treino.values.squeeze(),lags = 15)


# In[206]:


#Média móvel (MA)
sm.graphics.tsa.plot_pacf(infra_treino.values.squeeze(), lags = 15)


# # ####################
# # MODELO AUTO ARIMA - INFRAÇÕES
# # ####################

# # Auto ARIMA - Infrações

# In[248]:


#Criando o modelo do autoarima final
autoarima_infra = auto_arima(infra_treino, trace=True, seasonal = True, stationary = False, start_p = 1 , start_q = 1 , d = 5, max_p = 5 , max_q = 3, error_action='ignore', suppress_warnings=True, stepwise=True)
autoarima_infra_ajustado = autoarima_infra.fit(infra_treino)
autoarima_infra_ajustado.aic()


# In[249]:


autoarima_infra_ajustado.summary()


# In[209]:


# Reindexando Base teste
newindexteste1 = ['2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
infra_teste.reindex(newindexteste1)
infra_teste


# In[210]:


# Reindexando Base treino
newindextreino1 = ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03']
infra_treino.reindex(newindextreino1)
infra_treino


# In[211]:


# Criando o Forecast
forecast_autoarima_infra = autoarima_infra.predict(n_periods=len(infra_teste))
forecast_autoarima_infra = pd.DataFrame(forecast_autoarima_infra,index = infra_teste.index,columns=['Prediction'])


# In[239]:


# Plotando gráficos
plt.figure(figsize=(16,8))
plt.plot(infra_treino, label='Infrações base treino')
plt.plot(infra_teste, label='Infrações base teste')
plt.plot(forecast_autoarima_infra, label='Predição')
plt.legend(fontsize = 9)
plt.show()


# In[240]:


# Plotando gráficos
plt.figure(figsize=(16,8))
plt.plot(infra_teste, label='Infra base teste', color = 'orange')
plt.plot(forecast_autoarima_infra, label='Predição', color = 'green')
plt.title("Modelo ARIMA -- Infrações", fontsize=20)
plt.xlabel("Infrações", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.legend()
plt.show()


# # ################################################################
# # Análise de Desempenho do ARIMA 
# # ################################################################

# In[253]:


from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import mean_absolute_error


# In[412]:


# Comparando o AIC obtido para as bases
print("AIC ARIMA ACIDENTES")
print(autoarima_acid_ajustado.aic())

print("AIC ARIMA INFRAÇÕES")
print(autoarima_infra_ajustado.aic())


# In[262]:


# ARIMA - ACIDENTES
print("MSE - ARIMA ACIDENTES")
mean_forecast_error_acidarima = mean_squared_error(forecast_autoarima_acid, acid_teste)
print(mean_forecast_error_acidarima)
# ARIMA - INFRAÇÕES
print("MSE - INFRA INFRAÇÕES")
mean_forecast_error_infraarima = mean_squared_error(forecast_autoarima_infra, infra_teste)
print(mean_forecast_error_infraarima)


# # --------------------------------------------------------------------------------------------------------------
# # MODELO HOLT - WINTERS
# # -------------------------------------------------------------------------------------------------------------

# ### ACIDENTES

# In[214]:


import statsmodels.api as sm
from statsmodels.tsa.api import ExponentialSmoothing, Holt, SimpleExpSmoothing   


# In[215]:


# Aplicando modelo Holt-Winters - Acidentes

holtwint_acid = ExponentialSmoothing(acid_treino, seasonal_periods=12, trend="add", seasonal='add', use_boxcox=True, initialization_method="estimated")
holtwint_acid_ajustado = holtwint_acid.fit(optimized = True)


# In[216]:


holtwint_acid_ajustado.summary()


# In[217]:


# Criando Forecast
forecast_holtwint_acid = holtwint_acid_ajustado.forecast(9).rename("Holt Winters Seasonal - Acidentes")
forecast_holtwint_acid = forecast_holtwint_acid.set_axis(['2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-10', '2020-11'])
forecast_holtwint_acid


# In[218]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(acid_treino, marker="o", color = 'blue', label="Acidentes - base treino")
plt.plot(forecast_holtwint_acid, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(acid_teste, marker="o", color = "orange", label="Acidentes - base teste")
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt-Winters -- Acidentes RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=9)
plt.xticks([])
plt.show()


# In[219]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(forecast_holtwint_acid, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(acid_teste, marker="o", color = "orange", label="Acidentes - base teste")
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt-Winters -- Acidentes RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=9)
plt.show()


# ### INFRAÇÕES

# In[220]:


# Aplicando modelo Holt-Winters - Infrações

holtwint_infra = ExponentialSmoothing(infra_treino, seasonal_periods=12, trend="add", seasonal='add', use_boxcox=True, initialization_method="estimated")
holtwint_infra_ajustado = holtwint_infra.fit(optimized = True)


# In[221]:


holtwint_infra_ajustado.summary()


# In[222]:


# Criando Forecast
forecast_holtwint_infra = holtwint_infra_ajustado.forecast(9).rename("Holt Winters Seasonal - Infrações")
forecast_holtwint_infra = forecast_holtwint_infra.set_axis(['2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12'])


# In[223]:


infra_teste


# In[224]:


forecast_holtwint_infra


# In[225]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(infra_treino, marker="o", color = 'blue', label="Infrações - base treino")
plt.plot(forecast_holtwint_infra, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(infra_teste, marker="o", color = "orange", label="Infrações - base teste")
plt.xlabel("Infrações", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt-Winters -- Infrações RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=9)
plt.xticks([])
plt.show()


# In[226]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(forecast_holtwint_infra, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(infra_teste, marker="o", color = "orange", label="Infrações - base teste")
plt.xlabel("Infrações", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt-Winters -- Infrações RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=9)
plt.show()


# In[ ]:


# dESEMPENHO


# In[263]:


# HW - ACIDENTES
print("MSE - HW ACIDENTES")
mean_forecast_error_acidhw = mean_squared_error(forecast_holtwint_acid, acid_teste)
print(mean_forecast_error_acidhw)
# HW - INFRAÇÕES
print("MSE - HW INFRAÇÕES")
mean_forecast_error_infrahw = mean_squared_error(forecast_holtwint_infra, infra_teste)
print(mean_forecast_error_infrahw)


# In[ ]:





# In[ ]:





# # #################################################################
# # Holt Linear Trend

# ## Acidentes

# In[227]:


# Criando o Modelo
holtlin_acid = Holt(acid_treino, initialization_method="estimated")
holtlin_acid_ajustado = holtlin_acid.fit(smoothing_level=0.2, smoothing_trend=0.2, optimized=True)


# In[228]:


holtlin_acid_ajustado.summary()


# In[229]:


# Criando o forecast
forecast_holtlin_acid = holtlin_acid_ajustado.forecast(9).rename("Holt Linear Trend")
forecast_holtlin_acid = forecast_holtlin_acid.set_axis(['2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-10', '2020-11'])


# In[230]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(acid_treino, marker="o", color = 'blue', label="Acidentes - base treino")
plt.plot(forecast_holtlin_acid, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(acid_teste, marker="o", color = "orange", label="Acidentes - base teste")
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt Linear Trend -- Infrações RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=9)
plt.xticks([])
plt.show()


# In[231]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(forecast_holtlin_acid, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(acid_teste, marker="o", color = "orange", label="Acidentes - base teste")
plt.xlabel("Acidentes", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt Linear Trend -- Acidentes RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=12)
plt.show()


# ## Infrações

# In[232]:


# Criando o Modelo
holtlin_infra = Holt(infra_treino, initialization_method="estimated")
holtlin_infra_ajustado = holtlin_infra.fit(smoothing_level=0.2, smoothing_trend=0.2, optimized=True)


# In[233]:


holtlin_infra_ajustado.summary()


# In[234]:


# Criando o forecast
forecast_holtlin_infra = holtlin_infra_ajustado.forecast(9).rename("Holt Linear Trend")
forecast_holtlin_infra = forecast_holtlin_infra.set_axis(['2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12'])


# In[235]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(infra_treino, marker="o", color = 'blue', label="Infrações - base treino")
plt.plot(forecast_holtlin_infra, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(infra_teste, marker="o", color = "orange", label="Infrações - base teste")
plt.xlabel("Infrações", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt Linear Trend -- Infrações RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=12)
plt.xticks([])
plt.show()


# In[236]:


# Plotando os gráficos

plt.figure(figsize=(16,8))
plt.plot(forecast_holtlin_infra, marker = "o", color = "green", label = "Predição do Modelo")
plt.plot(infra_teste, marker="o", color = "orange", label="Infrações - base teste")
plt.xlabel("Infrações", fontsize = 16)
plt.ylabel("Mês-Ano", fontsize = 16)
plt.title("Modelo Holt Linear Trend -- Infrações RJ", fontsize = 20)
plt.rcParams.update({'font.size': 12})
plt.legend(fontsize=12)
plt.show()


# In[264]:


# Holt linear trend - ACIDENTES
print("MSE - HLT ACIDENTES")
mean_forecast_error_acidhlt = mean_squared_error(forecast_holtlin_acid, acid_teste)
print(mean_forecast_error_acidhlt)
# Holt Linear Trend - INFRAÇÕES
print("MSE - HLT INFRAÇÕES")
mean_forecast_error_infrahlt = mean_squared_error(forecast_holtlin_infra, infra_teste)
print(mean_forecast_error_infrahlt)


# # Desempenho geral Comparativo de Modelos
# 

# In[265]:


# Holt linear trend - ACIDENTES
print("MSE - HLT ACIDENTES")
mean_forecast_error_acidhlt = mean_squared_error(forecast_holtlin_acid, acid_teste)
print(mean_forecast_error_acidhlt)
# Holt Linear Trend - INFRAÇÕES
print("MSE - HLT INFRAÇÕES")
mean_forecast_error_infrahlt = mean_squared_error(forecast_holtlin_infra, infra_teste)
print(mean_forecast_error_infrahlt)

# Holt Winters - ACIDENTES
print("MSE - HW ACIDENTES")
mean_forecast_error_acidhw = mean_squared_error(forecast_holtwint_acid, acid_teste)
print(mean_forecast_error_acidhw)
# Holt Winters - INFRAÇÕES
print("MSE - HW INFRAÇÕES")
mean_forecast_error_infrahw = mean_squared_error(forecast_holtwint_infra, infra_teste)
print(mean_forecast_error_infrahw)

# ARIMA - ACIDENTES
print("MSE - ARIMA ACIDENTES")
mean_forecast_error_acidarima = mean_squared_error(forecast_autoarima_acid, acid_teste)
print(mean_forecast_error_acidarima)
# ARIMA - INFRAÇÕES
print("MSE - INFRA INFRAÇÕES")
mean_forecast_error_infraarima = mean_squared_error(forecast_autoarima_infra, infra_teste)
print(mean_forecast_error_infraarima)

