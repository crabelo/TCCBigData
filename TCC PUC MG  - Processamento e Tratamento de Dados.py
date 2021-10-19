#!/usr/bin/env python
# coding: utf-8

# # PUC - MG : Pós Graduação em Ciência de Dados e Big Data
# 
# #### ESTUDO E PREDIÇÃO DO COMPORTAMENTO DE INFRAÇÕES E ACIDENTES DE TRANSITO EM RODOVIAS FEDERAIS DO RIO DE JANEIRO
# #### Aluna: Camila da Mata Rabelo

# Coleta das bases de infrações e acidentes nos sites:
# 
# #Infrações: https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-infracoes
# 
# #Acidentes: https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes 

# In[1]:


#Carregar bibliotecas gerais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import datetime


# In[14]:


#Os arquivos foram descompactados manualmente
#Renomeados todos para jan, fev, mar....
#Renomeadas as pastas para ficarem padronizadas anoXXXX


# In[2]:


#Lendo o arquivo de infrações dos meses por ano
#Ano 2017
jan2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\jan.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
fev2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\fev.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
mar2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\mar.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
abr2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\abr.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
mai2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\mai.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
jun2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\jun.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
jul2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\jul.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
ago2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\ago.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
set2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\set.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
out2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\out.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
nov2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\nov.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
dez2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2017\dez.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')


# In[3]:


# Depois de verificar o shape de cada arquivo, vamos concatenar
ano2017 = pd.concat([jan2017, fev2017, mar2017, abr2017, mai2017, jun2017, jul2017, ago2017, set2017, out2017, nov2017, dez2017], join = "inner")
ano2017.head(1)


# In[4]:


#Lendo o arquivo de infrações dos meses por ano
#Ano 2018
jan2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\jan.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
fev2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\fev.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
mar2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\mar.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
abr2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\abr.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
mai2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\mai.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
jun2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\jun.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
jul2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\jul.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
ago2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\ago.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
set2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\set.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
out2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\out.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
nov2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\nov.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')
dez2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2018\dez.csv", sep=',', decimal = '.', encoding = "cp1252", dtype = 'object')


# In[5]:


# Depois de avaliar o shape de cada um, vamos concatenar
ano2018 = pd.concat([jan2018, fev2018, mar2018, abr2018, mai2018, jun2018, jul2018, ago2018, set2018, out2018, nov2018, dez2018], join = "inner")
ano2018.info()


# In[6]:


#Lendo o arquivo de infrações dos meses por ano
#Ano 2019
jan2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\jan.csv", sep = ';', encoding = "utf8", dtype = 'object')
fev2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\fev.csv", sep = ';', encoding = "utf8", dtype = 'object')
mar2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\mar.csv", sep = ';', encoding = "utf8", dtype = 'object')
abr2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\abr.csv", sep = ';', encoding = "utf8", dtype = 'object')
mai2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\mai.csv", sep = ';', encoding = "utf8", dtype = 'object')
jun2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\jun.csv", sep = ';', encoding = "utf8", dtype = 'object')
jul2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\jul.csv", sep = ';', encoding = "utf8", dtype = 'object')
ago2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\ago.csv", sep = ';', encoding = "utf8", dtype = 'object')
set2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\set.csv", sep = ';', encoding = "utf8", dtype = 'object')
out2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\out.csv", sep = ';', encoding = "utf8", dtype = 'object')
nov2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\nov.csv", sep = ';', encoding = "utf8", dtype = 'object')
dez2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2019\dez.csv", sep = ';', encoding = "utf8", dtype = 'object')
# explicar q o encoding cp1252 n funcionou


# In[7]:


# Depois de verificar os shapes dos arquivos, vamos concatenar
ano2019 = pd.concat([jan2019, fev2019, mar2019, abr2019, mai2019, jun2019, jul2019, ago2019, set2019, out2019, nov2019, dez2019], join = "inner")
ano2019.info()


# In[8]:


#Lendo o arquivo de infrações dos meses por ano
#Ano 2020
jan2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\jan.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
fev2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\fev.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
mar2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\mar.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
abr2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\abr.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
mai2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\mai.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
jun2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\jun.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
jul2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\jul.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
ago2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\ago.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
set2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\set.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
out2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\out.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
nov2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\nov.csv", sep = ';', encoding = 'cp1252', dtype = 'object')
dez2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Infracoes\ano2020\dez.csv", sep = ';', encoding = 'cp1252', dtype = 'object')


# In[9]:


# a base de Janeiro de 2020 tem uma coluna a mais do que as outras, por isso precisaremos deletá-la antes de concatenar 
# todos os meses de 2020
del jan2020['UF Placa']
#Agora sim, vamos unir todos os meses
ano2020 = pd.concat([jan2020, fev2020, mar2020, abr2020, mai2020, jun2020, jul2020, ago2020, set2020, out2020, nov2020, dez2020], join = "inner")
ano2020.info()


# # ------------------------------------------------------------------------------------------------------------
# # Processamento e Tratamento das bases
# # ------------------------------------------------------------------------------------------------------------

# ## Higienização de ano2017 - Uniformização das colunas

# In[10]:


#Verificando as colunas no dataframe para  verificar quais serão deletadas
ano2017.columns.tolist()


# In[11]:


#Ano2017 - Eliminando colunas que não serão usadas
ano2017a = ano2017.drop(columns=['tip_abordagem', 'ind_assinou_auto','ind_veiculo_estrangeiro', 'ind_sentido_trafego', 'uf_placa','enquadramento', 'data_inicio_vigencia', 'data_fim_vigencia', 'med_realizada', 'med_considerada','especie', 'nome_veiculo_marca', 'nom_modelo_veiculo', 'exc_verificado',  'num_km_infracao', 'nom_municipio'],axis=1)
ano2017a.head()


# In[12]:


#Uma vez que já vimos que a coluna de hora está como 00:00:00 vamos nomeá-la de uma forma provisória, pois vamos criar outra
ano2017a.columns = ['Data', 'UF',  'BR', 'Codigo', 'Descricao','Hora_infr_prov']
ano2017a.info()


# In[13]:


# Aqui criaremos outra coluna de hora, porém em formato inteiro
ano2017a['Hora'] = ano2017a['Hora_infr_prov'].str.split(':').str[0]
ano2017a.head(1)
#Agora deletaremos a coluna antiga
del ano2017a['Hora_infr_prov']
ano2017a.info()


# In[14]:


#Verificando colunas com valores NaN
ano2017a.isnull().sum()


# In[15]:


#Deletaremos agora as linhas NaN presentes
ano2017b = ano2017a.dropna(subset = ['Hora'])
ano2017b.isnull().sum()


# In[16]:


#Verificando o tipo de dados das colunas
ano2017b.info()


# In[17]:


# Formatando tipo das colunas
# OBS. Vamos manter data ainda como object para fazermos a identificação de MÊS
ano2017c = ano2017b.astype({"BR": int, "Hora": int, "Codigo": int})
ano2017c.info()


# ## Higienização ano2018  - Uniformização das colunas

# In[18]:


#Verificando as colunas no dataframe para  verificar quais serão deletadas
ano2018.columns.tolist()


# In[19]:


#Ano2018 - Eliminando colunas que não serão usadas
ano2018a = ano2018.drop(columns=['tip_abordagem', 'ind_assinou_auto','ind_veiculo_estrangeiro', 'ind_sentido_trafego', 'uf_placa','enquadramento', 'data_inicio_vigencia', 'data_fim_vigencia', 'med_realizada', 'med_considerada','especie', 'nome_veiculo_marca', 'nom_modelo_veiculo', 'exc_verificado',  'num_km_infracao', 'nom_municipio'],axis=1)
ano2018a.info()


# In[20]:


#Uma vez que já vimos que a coluna de hora está como 00:00:00 vamos nomeá-la de uma forma provisória, pois vamos criar outra
ano2018a.columns = ['Data', 'UF',  'BR', 'Codigo', 'Descricao','Hora_infr_prov']
ano2018a.info()


# In[21]:


# Aqui criaremos outra coluna de hora, porém em formato inteiro
ano2018a['Hora'] = ano2018a['Hora_infr_prov'].str.split(':').str[0]
# Agora deletaremos a coluna antiga
del ano2018a['Hora_infr_prov']
ano2018a.head(1)


# In[22]:


ano2018a.isnull().sum()


# In[23]:


#Deletar linhas nulas da coluna de Hora
ano2018b = ano2018a.dropna(subset = ['Hora'])
ano2018b.isnull().sum()
#Não converti aqui o astype(int) porque isso torna o DF emm SERIE e aí não dá pra agrupar


# In[24]:


#Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS
ano2018c = ano2018b.astype({"BR": int, "Hora": int, "Codigo": int})
ano2018c.info()


# ## Higienizando ano2019 - Uniformização das colunas

# In[25]:


# Verificando colunas 
ano2019.columns.tolist()


# In[26]:


#Ano2019 - Eliminando colunas que não serão usadas
ano2019a = ano2019.drop(columns=['Número do Auto', 'Indicador de Abordagem', 'Assinatura do Auto', 'Indicador Veiculo Estrangeiro', 'Sentido Trafego', 'UF Placa','Enquadramento da Infração', 'Início Vigência da Infração', 'Fim Vigência Infração', 'Medição Infração', 'Descrição Especie Veículo', 'Descrição Marca Veículo','Medição Considerada', 'Excesso Verificado',  'Km Infração', 'Município'],axis=1)
ano2019a.info()


# In[27]:


#Renomear para o padrão usado em 2017 e 2018
ano2019a.columns = ['Data', 'UF',  'BR', 'Codigo', 'Descricao', 'Hora']
ano2019a.info()


# In[28]:


# Verificando se há linhas nulas
ano2019a.isnull().sum()


# In[29]:


# Não há linhas nulas
# Mas o processo será realizado da mesma forma para manter a lógica da nomenclatura
ano2019b = ano2019a.dropna(subset = ['Hora'])
ano2019b.isnull().sum()

#Não converti aqui o astype(int) pq isso torna o DF emm SERIE e aí não dá pra agrupar


# In[30]:


#Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS
ano2019c = ano2019b.astype({"BR": int, "Hora": int, "Codigo": int})
ano2019c.info()


# ## Higienização de ano2020 - Uniformização das colunas

# In[31]:


# Verificando as colunas
ano2020.columns.tolist()


# In[32]:


#Ano2020 - Eliminando colunas que não serão usadas
ano2020a = ano2020.drop(columns=['Número do Auto', 'Indicador de Abordagem', 'Assinatura do Auto', 'Indicador Veiculo Estrangeiro', 'Sentido Trafego', 'Enquadramento da Infração', 'Início Vigência da Infração', 'Fim Vigência Infração', 'Medição Infração', 'Descrição Especie Veículo', 'Descrição Marca Veículo','Medição Considerada','Qtd Infrações',  'Excesso Verificado',  'Km Infração', 'Município'],axis=1)
ano2020a.info()


# In[33]:


# Renomear para o padrão usado
ano2020a.columns = ['Data', 'UF',  'BR', 'Codigo', 'Descricao', 'Hora']
ano2020a.head(1)


# In[34]:


# Verificando se há linhas nulas
ano2020a.isnull().sum()


# In[35]:


# Não há linhas nulas, mas procederemos com o comando mesmo assim, para mantermos o padrão de nomes de dataframes
ano2020b = ano2020a.dropna(subset = ['Hora'])
ano2020b.info()
#Não converti aqui o astype(int) pq isso torna o DF emm SERIE e aí não dá pra agrupar


# In[36]:


#Formatando tipo das colunas
# Vamos manter Data ainda como object pra fazer a identificação de MÊS
ano2020c = ano2020b.astype({"BR": int, "Hora": int, "Codigo": int})
ano2020c.info()


# # ##################################################################
# 
# #           INFRAÇÕES    POR UF        
# # ##################################################################

# ## Ranking e gráfico de Infrações por UF - 2017

# In[37]:


# Agrupando infrações do ano por UF
ano2017_ufs = ano2017c.groupby(['UF']).size().sort_values(ascending=False)
ano2017_ufs = ano2017_ufs.rename("Total de Infrações por ano")
ano2017_ufs.rename_axis("Total de infrações por ano")
ano2017_ufs


# In[38]:


type(ano2017_ufs)


# In[39]:


# Gráfico de Infrações por UF - 2017
ano2017_ufs.plot.bar(figsize=(10,8), color = 'lightpink', title = "Gráfico de Infrações por UF - 2017", ylabel = 'Infrações')


# ## Ranking e gráfico de Infrações por UF - 2018

# In[40]:


# Agrupando infrações do ano por UF
ano2018_ufs = ano2018c.groupby(['UF']).size().sort_values(ascending=False)
ano2018_ufs = ano2018_ufs.rename("Total de Infrações por ano")
ano2018_ufs


# In[41]:


type(ano2018_ufs)


# In[42]:


# Gráfico de Infrações por UF - 2018
ano2018_ufs.plot.bar(figsize=(10,8), color = 'lightpink', title = "Gráfico de Infrações por UF - 2018", ylabel = 'Infrações')


# ## Ranking e gráfico de Infrações por UF - 2019

# In[43]:


# Agrupando infrações do ano por UF
ano2019_ufs = ano2019c.groupby(['UF']).size().sort_values(ascending=False)
ano2019_ufs = ano2019_ufs.rename("Total de Infrações por ano")
ano2019_ufs


# In[44]:


type(ano2019_ufs)


# In[45]:


# Gráfico de Infrações por UF - 2019
ano2019_ufs.plot.bar(figsize=(10,8), color = 'lightpink', title = 'Gráfico de Infrações por UF - 2019', ylabel = 'Infrações')


# ## Ranking e gráfico de Infrações por UF - 2020

# In[46]:


# Agrupando infrações do ano por UF
ano2020_ufs = ano2020c.groupby(['UF']).size().sort_values(ascending=False)
ano2020_ufs = ano2020_ufs.rename("Total de Infrações por ano")
ano2020_ufs


# In[47]:


type(ano2020_ufs)


# In[48]:


# Gráfico de Infrações por UF - 2020
ano2020_ufs.plot.bar(figsize=(10,8), color = 'lightpink', title = 'Gráfico de Infrações por UF - 2020', ylabel = 'Infrações')


# # ################################################################
# # DATASET  ACIDENTES
# #  ################################################################

# In[49]:


#Lendo o arquivo de infrações dos meses por ano

acid2017 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Acidentes\acidentes2017_todas_causas_tipos.csv", sep=';', decimal = '.', encoding = 'cp1252', dtype = 'object')
acid2018 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Acidentes\acidentes2018_todas_causas_tipos.csv", sep=';', decimal = '.', encoding = 'cp1252', dtype = 'object')
acid2019 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Acidentes\acidentes2019_todas_causas_tipos.csv", sep=';', decimal = '.', encoding = 'cp1252', dtype = 'object')
acid2020 = pd.read_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Acidentes\acidentes2020_todas_causas_tipos.csv", sep=';', decimal = '.', encoding = 'utf8', dtype = 'object')


# In[50]:


# Usando cp1252 na planilha de 2020 deu erro de
#"UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 4165: character maps to <undefined>"
# por isso decidi usar outro encoding.


# # HIGIENIZAÇÃO ACIDENTES

# # Ano 2017

# In[51]:


# Avaliando a base
acid2017.columns.tolist()


# In[52]:


#Acid2017 - Eliminando colunas que não serão usadas
acid2017a = acid2017.drop(columns=['id', 'pesid', 'causa_principal', 'ordem_tipo_acidente','fase_dia', 'sentido_via', 'condicao_metereologica','tipo_pista','tracado_via', 'uso_solo', 'id_veiculo', 'tipo_veiculo', 'marca', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'estado_fisico', 'idade', 'sexo','regional', 'delegacia', 'uop','latitude','longitude', 'municipio', 'km'],axis=1)
acid2017a.info()


# In[53]:


# Criando coluna de hora inteira
acid2017a['Hora'] = acid2017a['horario'].str.split(':').str[0]

#Deletando a coluna antiga
del acid2017a['horario']
acid2017a.info()


# In[54]:


# Renomear a base para o padrão usado
acid2017a.columns = ['Data', 'Dia_semana', 'UF',  'BR', 'Causa', 'Tipo_acidente','Classificacao', 'Ilesos', 'Feridos_leves', 'Feridos_graves', 'Obitos', 'Hora']
acid2017a.info()


# In[55]:


# Verificando se há linhas nulas
acid2017a.isnull().sum()


# In[56]:


#Deletaremos agora as linhas nulas
acid2017b = acid2017a.dropna(subset = ['BR'])
acid2017b.isnull().sum()


# In[57]:


# Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS

acid2017c = acid2017b.astype({"BR": int, "Hora": int, 'Ilesos': int, 'Feridos_leves' : int, 'Feridos_graves': int, 'Obitos' : int})
acid2017c.info()


# # ANO 2018

# In[58]:


# Verificando a base
acid2018.info()


# In[59]:


#Acid2018 - Eliminando colunas que não serão usadas
acid2018a = acid2018.drop(columns=['id', 'pesid', 'causa_principal', 'ordem_tipo_acidente','fase_dia', 'sentido_via', 'condicao_metereologica','tipo_pista','tracado_via', 'uso_solo', 'id_veiculo', 'tipo_veiculo', 'marca', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'estado_fisico', 'idade', 'sexo','regional', 'delegacia', 'uop', 'km',  'latitude', 'longitude', 'municipio'] ,axis=1)
acid2018a.info()


# In[60]:


# Criando coluna de hora inteira
acid2018a['Hora'] = acid2018a['horario'].str.split(':').str[0]

#Deletando horario
del acid2018a['horario']
acid2018a.info()


# In[61]:


# Renomeando colunas para o padrão usado
acid2018a.columns = ['Data', 'Dia_semana', 'UF',  'BR', 'Causa', 'Tipo_acidente','Classificacao', 'Ilesos', 'Feridos_leves', 'Feridos_graves', 'Obitos', 'Hora']
acid2018a.info()


# In[62]:


# Verificando se há linhas nulas
acid2018a.isnull().sum()


# In[63]:


# Deletaremos agora as linhas nulas
acid2018b = acid2018a.dropna(subset = ['BR'])
acid2018b = acid2018b.dropna(subset = ['Tipo_acidente'])
acid2018b.isnull().sum()


# In[64]:


#Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS
acid2018c = acid2018b.astype({"BR": int, "Hora": int, 'Ilesos': int, 'Feridos_leves' : int, 'Feridos_graves': int, 'Obitos' : int})
acid2018c.info()


# # Ano 2019

# In[65]:


# Verificando a base
acid2019.info()


# In[66]:


#Acid2019 - Eliminando colunas que não serão usadas
acid2019a = acid2019.drop(columns=['id', 'pesid', 'km', 'causa_principal', 'ordem_tipo_acidente','fase_dia', 'sentido_via', 'condicao_metereologica','tipo_pista','tracado_via', 'uso_solo', 'id_veiculo', 'tipo_veiculo', 'marca', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'estado_fisico', 'idade', 'sexo','regional', 'delegacia', 'uop',  'latitude','longitude', 'municipio'],axis=1)
acid2019a.info()


# In[67]:


# Criando coluna de hora inteira
acid2019a['Hora'] = acid2019a['horario'].str.split(':').str[0]

#Deletando a coluna antiga de horário
del acid2019a['horario']
acid2019a.info()


# In[68]:


# Renomeando para o padrão usado
acid2019a.columns = ['Data', 'Dia_semana', 'UF',  'BR', 'Causa', 'Tipo_acidente','Classificacao', 'Ilesos', 'Feridos_leves', 'Feridos_graves', 'Obitos', 'Hora']
acid2019a.info()


# In[69]:


# Verificando se há linhas nulas
acid2019a.isnull().sum()


# In[70]:


#Deletaremos as linhas nulas
acid2019b = acid2019a.dropna(subset = ['BR'])
acid2019b = acid2019b.dropna(subset = ['Tipo_acidente'])
acid2019b.isnull().sum()


# In[71]:


#Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS
acid2019c = acid2019b.astype({"BR": int, "Hora": int, 'Ilesos': int, 'Feridos_leves' : int, 'Feridos_graves': int, 'Obitos' : int})
acid2019c.info()


# ## Ano 2020

# In[72]:


# Verificando a base
acid2020.info()


# In[73]:


#Acid2020 - Eliminando as colunas que não serão usadas
acid2020a = acid2020.drop(columns=['id', 'pesid', 'km', 'causa_principal', 'ordem_tipo_acidente','fase_dia', 'sentido_via', 'condicao_metereologica','tipo_pista','tracado_via', 'uso_solo', 'id_veiculo', 'tipo_veiculo', 'marca', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'estado_fisico', 'idade', 'sexo','regional', 'delegacia', 'uop',  'latitude','longitude', 'municipio'], axis = 1)
acid2020a.info()


# In[74]:


# Criando coluna de hora inteira
acid2020a['Hora'] = acid2020a['horario'].str.split(':').str[0]

#Deletando coluna antiga de horário
del acid2020a['horario']
acid2020a.info()


# In[75]:


# Renomeando para o padrão usado
acid2020a.columns = ['Data', 'Dia_semana', 'UF',  'BR', 'Causa', 'Tipo_acidente','Classificacao', 'Ilesos', 'Feridos_leves', 'Feridos_graves', 'Obitos', 'Hora']
acid2020a.info()


# In[76]:


# Verificando se há linhas nulas
acid2020a.isnull().sum()


# In[77]:


#Deletaremos agora as linhas nulas
acid2020b = acid2020a.dropna(subset = ['BR'])
acid2020b = acid2020b.dropna(subset = ['Tipo_acidente'])
acid2020b.isnull().sum()


# In[78]:


#Formatando tipo das colunas
# Vamos manter data ainda como object pra fazer a identificação de MÊS
acid2020c = acid2020b.astype({"BR": int, "Hora": int, 'Ilesos': int, 'Feridos_leves' : int, 'Feridos_graves': int, 'Obitos' : int})
acid2020c.info()


# # Análise do estado com mais acidentes

# # Ranking e gráfico de acidentes por UF - 2017

# In[79]:


# Agrupando acidentes por UF - 2017
acid2017top = acid2017c.groupby("UF").size().sort_values(ascending=False)
acid2017top = acid2017top.rename("Total de acidentes por ano")
acid2017top


# In[80]:


# Gráfico de Acidentes por UF - 2017
acid2017top.plot.bar(figsize=(10,8), color = 'lightblue', title = "Gráfico de Acidentes por UF - 2017", ylabel = 'Acidentes')


# # Ranking e gráfico de acidentes por UF - 2018

# In[81]:


# Agrupando acidentes por UF
acid2018top = acid2018c.groupby("UF").size().sort_values(ascending=False)
acid2018top = acid2018top.rename("Total de acidentes por ano")
acid2018top


# In[82]:


# Gráfico de Acidentes por UF - 2018
acid2018top.plot.bar(figsize=(10,8), color = 'lightblue', title = "Gráfico de Acidentes por UF - 2018", ylabel = 'Acidentes')


# # Ranking e gráfico de acidentes por UF - 2019

# In[83]:


# Agrupando acidentes por UF
acid2019top = acid2019c.groupby("UF").size().sort_values(ascending=False)
acid2019top = acid2019top.rename("Total de acidentes por ano")
acid2019top


# In[84]:


# Gráfico de Acidentes por UF - 2019
acid2019top.plot.bar(figsize=(10,8), color = 'lightblue', title = "Gráfico de Acidentes por UF - 2019", ylabel = 'Acidentes')


# # Ranking e gráfico de acidentes por UF - 2020

# In[85]:


# Agrupando acidentes por UF - 2020
acid2020top = acid2020c.groupby("UF").size().sort_values(ascending=False)
acid2020top = acid2020top.rename("Total de acidentes por ano")
acid2020top


# In[86]:


# Gráfico de Acidentes por UF - 2020
acid2020top.plot.bar(figsize=(10,8), color = 'lightblue', title = "Gráfico de Acidentes por UF - 2020", ylabel = 'Acidentes')


# # ################################################################
# #                     Mergir o top infrações com top acidentes UF
# # ################################################################

# ## Ano 2017

# In[87]:


# Mergindo o ranking de infrações por UF com o ranking de acidentes por UF - 2017
print ("UFs com maior ocorrências de infrações e acidentes - 2017")
toptotal2017 = pd.merge(ano2017_ufs, acid2017top, how ='left',  on = ['UF'])
toptotal2017['Infrações + Acidentes'] = (toptotal2017['Total de Infrações por ano'] + toptotal2017['Total de acidentes por ano'])
toptotal2017.sort_values(ascending = False, by = 'Infrações + Acidentes')[:5]


# ## Ano 2018

# In[88]:


# Mergindo o ranking de infrações por UF com o ranking de acidentes por UF - 2018
print ("UFs com maior ocorrências de infrações e acidentes - 2018")
toptotal2018 = pd.merge(ano2018_ufs, acid2018top, how ='left',  on = ['UF'])
toptotal2018['Infrações + Acidentes'] = (toptotal2018['Total de Infrações por ano'] + toptotal2018['Total de acidentes por ano'])
toptotal2018.sort_values(ascending = False, by = 'Infrações + Acidentes')[:5]


# ## Ano 2019

# In[89]:


# Mergindo o ranking de infrações por UF com o ranking de acidentes por UF - 2019
print ("UFs com maior ocorrências de infrações e acidentes - 2019")
toptotal2019 = pd.merge(ano2019_ufs, acid2019top, how ='left',  on = ['UF'])
toptotal2019['Infrações + Acidentes'] = (toptotal2019['Total de Infrações por ano'] + toptotal2019['Total de acidentes por ano'])
toptotal2019.sort_values(ascending = False, by = 'Infrações + Acidentes')[:5]


# ## Ano 2020

# In[90]:


# Mergindo o ranking de infrações por UF com o ranking de acidentes por UF - 2020
print ("UFs com maior ocorrências de infrações e acidentes - 2020")
toptotal2020 = pd.merge(ano2020_ufs, acid2020top, how ='left',  on = ['UF'])
toptotal2020['Infrações + Acidentes'] = (toptotal2020['Total de Infrações por ano'] + toptotal2020['Total de acidentes por ano'])
toptotal2020.sort_values(ascending = False, by = 'Infrações + Acidentes')[:5]


# ### Foi decidido então que o estado foco do projeto seria o Rio de Janeiro

# # Filtrando: estado do Rio de Janeiro

# ## Ano 2017

# In[91]:


# INFRAÇÕES RIO DE JANEIRO 2017
estado = ['RJ']
inf2017rj = ano2017c[ano2017c['UF'].isin(estado)]
inf2017rj.info(0)


# In[92]:


# ACIDENTES RIO DE JANEIRO 2017
estado = ['RJ']
acid17rj = acid2017c[acid2017c['UF'].isin(estado)]
acid17rj.head(2)
acid17rj.info()


# ## Ano 2018

# In[93]:


# INFRAÇÕES RIO DE JANEIRO 2018
estado = ['RJ']
inf2018rj = ano2018c[ano2018c['UF'].isin(estado)]
inf2018rj.info()


# In[94]:


# ACIDENTES RIO DE JANEIRO 2018
estado = ['RJ']
acid18rj = acid2018c[acid2018c['UF'].isin(estado)]
acid18rj.info()


# ## Ano 2019

# In[95]:


# INFRAÇÕES RIO DE JANEIRO 2019
estado = ['RJ']
inf2019rj = ano2019c[ano2019c['UF'].isin(estado)]
inf2019rj.info()


# In[96]:


# ACIDENTES RIO DE JANEIRO 2019
estado = ['RJ']
acid19rj = acid2019c[acid2019c['UF'].isin(estado)]
acid19rj.info()


# ## Ano 2020

# In[97]:


# INFRAÇÕES RIO DE JANEIRO 2020
estado = ['RJ']
inf2020rj = ano2020c[ano2020c['UF'].isin(estado)]
inf2020rj.info()


# In[98]:


# ACIDENTES RIO DE JANEIRO 2020
estado = ['RJ']
acid20rj = acid2020c[acid2020c['UF'].isin(estado)]
acid20rj.info()


# #  ################################################################
# # DATASET CLASSIFICAÇÃO DAS INFRAÇÕES
# # ################################################################

# In[99]:


#Lendo o arquivo de tipos de infrações
tiposdeinfracoes = pd.read_excel(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Tipos\tabela_infracoes.xlsx", squeeze=True, dtype = 'object')


# In[100]:


# Verificando a base
tiposdeinfracoes.columns.tolist()


# In[101]:


# Tiposdeinfracao - Eliminando colunas que não serão usadas
tipos_infra = tiposdeinfracoes.drop(columns = ['INFRAÇÃO', 'ARTIGOS DO CTB', 'VALOR DA MULTA'], axis = 1)

# Renomeando para o padrão
tipos_infra.rename(columns = {'CÓDIGO DA INFRAÇÃO':'Codigo','RESPONSÁVEL' : 'Responsavel'}, inplace = True)

# Alterando o tipo de dados da coluna
tipos_infra = tipos_infra.astype({"Codigo": int})
tipos_infra.info()


# ### Mergindo com inf2017rj

# In[102]:


# Mergindo a base tiposdeinfracao com base de infrações RJ - 2017
infra17rj = pd.merge(inf2017rj, tipos_infra, on ='Codigo', how ='left')

# Verificando se há linhas nulas
infra17rj.isnull().sum()


# In[103]:


# Deletaremos as linhas nulas
infra17rj = infra17rj.dropna(subset = ['Tipo'])
infra17rj.isnull().sum()


# In[104]:


# Verificando a nova base
infra17rj.info()


# ### Mergindo com inf2018rj

# In[105]:


# Mergindo a base tiposdeinfracao com base de infrações RJ - 2018
infra18rj = pd.merge(inf2018rj, tipos_infra, on ='Codigo', how ='left')

# Verificando se há linhas nulas
infra18rj.isnull().sum()


# In[106]:


# Deletaremos as linhas nulas
infra18rj = infra18rj.dropna(subset = ['Tipo'])
infra18rj.isnull().sum()


# In[107]:


# Verificando a nova base
infra18rj.info()


# ### Mergindo com inf2019rj

# In[108]:


# Mergindo a base tiposdeinfracao com base de infrações RJ - 2019
infra19rj = pd.merge(inf2019rj, tipos_infra, on ='Codigo', how ='left')

#Verificando se há linhas nulas
infra19rj.isnull().sum()


# In[109]:


# Deletaremos as linhas nulas
infra19rj = infra19rj.dropna(subset = ['Tipo'])
infra19rj.isnull().sum()


# In[110]:


# Verificando a nova base
infra19rj.info()


# ### Mergindo com inf2020rj

# In[111]:


# Mergindo a base tiposdeinfracao com base de infrações RJ - 2020
infra20rj = pd.merge(inf2020rj, tipos_infra, on ='Codigo', how ='left')

# Verificando se há linhas nulas
infra20rj.isnull().sum()


# In[112]:


# Deletaremos as linhas nulas
infra20rj = infra20rj.dropna(subset = ['Tipo'])
infra20rj.isnull().sum()


# In[113]:


# Verificando a nova base
infra20rj.info()


# ## Adicionaremos coluna de PERÍODO DO DIA

# In[114]:


# Primeiramente criaremos cópias dos dataframes de infrações usados

import copy
infra17rj_copy = pd.DataFrame(columns = infra17rj.columns, data = copy.deepcopy(infra17rj.values))
print ("Infrações RJ 2017 - completa")
infra18rj_copy = pd.DataFrame(columns = infra18rj.columns, data = copy.deepcopy(infra18rj.values))
print ("Infrações RJ 2018 - completa")
infra19rj_copy = pd.DataFrame(columns = infra19rj.columns, data = copy.deepcopy(infra19rj.values))
print ("Infrações RJ 2019 - completa")
infra20rj_copy = pd.DataFrame(columns = infra20rj.columns, data = copy.deepcopy(infra20rj.values))
print ("Infrações RJ 2020 - completa")


# In[115]:


# Agora criaremos cópias dos dataframes de acidentes

acid17rj_copy = pd.DataFrame(columns = acid17rj.columns, data = copy.deepcopy(acid17rj.values))
print ("Acidentes RJ 2017 - completa")
acid18rj_copy = pd.DataFrame(columns = acid18rj.columns, data = copy.deepcopy(acid18rj.values))
print ("Acidentes RJ 2018 - completa")
acid19rj_copy = pd.DataFrame(columns = acid19rj.columns, data = copy.deepcopy(acid19rj.values))
print ("Acidentes RJ 2019 - completa")
acid20rj_copy = pd.DataFrame(columns = acid20rj.columns, data = copy.deepcopy(acid20rj.values))
print ("Acidentes RJ 2020 - completa")


# In[116]:


# Verificaremos as cópias de infrações
print ("Infrações RJ 2017")
infra17rj_copy.info()
print ("Infrações RJ 2018")
infra18rj_copy.info()
print ("Infrações RJ 2019")
infra19rj_copy.info()
print ("Infrações RJ 2020")
infra20rj_copy.info()
print ("Cópias realizadas")


# In[117]:


# E agora verificaremos as cópias de acidentes
print ("Acidentes RJ 2017")
acid17rj_copy.info()
print ("Acidentes RJ 2018")
acid18rj_copy.info()
print ("Acidentes RJ 2019")
acid19rj_copy.info()
print ("Acidentes RJ 2020")
acid20rj_copy.info()


# In[118]:


# Precisamos definir a fórmula que irá dividir o dia em períodos

def f(Hora):
    if Hora>=0 and Hora<=5 :
        return "Madrugada"
    elif Hora>= 6 and Hora<= 11:
        return "Manhã"
    elif Hora>= 12 and Hora<= 17:
        return "Tarde"
    else:
        return "Noite"


# In[119]:


# Aplicando a fórmula - Inserindo coluna Período para bases de Infrações RJ
infra17rj_copy["Periodo"] = infra17rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2017 ok")
infra18rj_copy["Periodo"] = infra18rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2018 ok")
infra19rj_copy["Periodo"] = infra19rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2019 ok")
infra20rj_copy["Periodo"] = infra20rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2020 ok")


# In[120]:


## Aplicando a fórmula - Inserindo coluna Período para bases de Acidentes RJ
acid17rj_copy["Periodo"] = acid17rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2017 ok")
acid18rj_copy["Periodo"] = acid18rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2018 ok")
acid19rj_copy["Periodo"] = acid19rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2019 ok")
acid20rj_copy["Periodo"] = acid20rj_copy["Hora"].apply(lambda Hora: f(Hora))
print ("2020 ok")


# # O que temos agora são as seguintes bases:
# ### Infrações RJ por ano
# infra17rj_copy
# 
# infra18rj_copy
# 
# infra19rj_copy
# 
# infra20rj_copy
# 
# ### Acidentes RJ por ano
# acid17rj_copy
# 
# acid18rj_copy
# 
# acid19rj_copy
# 
# acid20rj_copy
# 

# In[121]:


#Aqui se verificou as linhas nulas e não havia nenhuma em nenhum DF
# ex: acid20rj_copy.isnull().sum()


# # Adicionando coluna Index Mês

# In[123]:


# Inserindo a coluna Index_mes em todas as bases

infra17rj_copy['Index_mes'] = infra17rj_copy['Data'].str.split('-').str[1]
print ("infra 2017 ok")
infra18rj_copy['Index_mes'] = infra18rj_copy['Data'].str.split('-').str[1]
print ("infra 2018 ok")
infra19rj_copy['Index_mes'] = infra19rj_copy['Data'].str.split('-').str[1]
print ("infra 2019 ok")
infra20rj_copy['Index_mes'] = infra20rj_copy['Data'].str.split('-').str[1]
print ("infra 2020 ok")

acid17rj_copy['Index_mes'] = acid17rj_copy['Data'].str.split('-').str[1]
print ("acid 2017 ok")
acid18rj_copy['Index_mes'] = acid18rj_copy['Data'].str.split('-').str[1]
print ("acid 2018 ok")
acid19rj_copy['Index_mes'] = acid19rj_copy['Data'].str.split('-').str[1]
print ("acid 2019 ok")
acid20rj_copy['Index_mes'] = acid20rj_copy['Data'].str.split('-').str[1]
print ("acid 2020 ok")


# # Criando a coluna ANO e ANO-MÊS

# In[126]:


#Criando coluna ano
infra17rj_copy['ano'] = infra17rj_copy['Data'].str.split('-').str[0]
infra18rj_copy['ano'] = infra18rj_copy['Data'].str.split('-').str[0]
infra19rj_copy['ano'] = infra19rj_copy['Data'].str.split('-').str[0]
infra20rj_copy['ano'] = infra20rj_copy['Data'].str.split('-').str[0]

acid17rj_copy['ano'] = acid17rj_copy['Data'].str.split('-').str[0]
acid18rj_copy['ano'] = acid18rj_copy['Data'].str.split('-').str[0]
acid19rj_copy['ano'] = acid19rj_copy['Data'].str.split('-').str[0]
acid20rj_copy['ano'] = acid20rj_copy['Data'].str.split('-').str[0]


# In[128]:


#Juntando ano com mês
infra17rj_copy['mes_ano'] = infra17rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
infra18rj_copy['mes_ano'] = infra18rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
infra19rj_copy['mes_ano'] = infra19rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
infra20rj_copy['mes_ano'] = infra20rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)

acid17rj_copy['mes_ano'] = acid17rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
acid18rj_copy['mes_ano'] = acid18rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
acid19rj_copy['mes_ano'] = acid19rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)
acid20rj_copy['mes_ano'] = acid20rj_copy[['ano', 'Index_mes']].agg('-'.join, axis=1)


# # Criando a coluna de Mês por nome de mês

# In[130]:


# Converter tipo da coluna Index_mes para inteiro

infra17rj_copy['Index_mes'] = pd.to_numeric(infra17rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("infra 2017 ok")
infra18rj_copy['Index_mes'] = pd.to_numeric(infra18rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("infra 2018 ok")
infra19rj_copy['Index_mes'] = pd.to_numeric(infra19rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("infra 2019 ok")
infra20rj_copy['Index_mes'] = pd.to_numeric(infra20rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("infra 2020 ok")

acid17rj_copy['Index_mes'] =  pd.to_numeric(acid17rj_copy['Index_mes'], errors="coerce").astype('int64')
print("acid 2017 ok")
acid18rj_copy['Index_mes'] =  pd.to_numeric(acid18rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("acid 2018 ok")
acid19rj_copy['Index_mes'] =  pd.to_numeric(acid19rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("acid 2019 ok")
acid20rj_copy['Index_mes'] =  pd.to_numeric(acid20rj_copy['Index_mes'], errors="coerce").astype('int64')
print ("acid 2020 ok")


# In[132]:


# Precisamos definir agora a fórmula que nos dará o nome do mês baseado no seu índice, Index_mes, criado anteriormente

def g(Index_mes):
    if Index_mes == 1 :
        return "Janeiro"
    elif Index_mes == 2:
        return "Fevereiro"
    elif Index_mes == 3:
        return "Março"
    elif Index_mes == 4:
        return "Abril"
    elif Index_mes == 5:
        return "Maio"
    elif Index_mes == 6:
        return "Junho"
    elif Index_mes == 7:
        return "Julho"
    elif Index_mes == 8:
        return "Agosto"
    elif Index_mes == 9:
        return "Setembro"
    elif Index_mes == 10:
        return "Outubro"
    elif Index_mes == 11:
        return "Novembro"
    else:
        return "Dezembro"


# In[133]:


# Inserindo coluna Mes para Infrações RJ

infra17rj_copy["Mes"] = infra17rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2017 ok")
infra18rj_copy["Mes"] = infra18rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2018 ok")
infra19rj_copy["Mes"] = infra19rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2019 ok")
infra20rj_copy["Mes"] = infra20rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2020 ok")


# In[134]:


# Inserindo coluna  Mes para Acidentes RJ

acid17rj_copy["Mes"] = acid17rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2017 ok")
acid18rj_copy["Mes"] = acid18rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2018 ok")
acid19rj_copy["Mes"] = acid19rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2019 ok")
acid20rj_copy["Mes"] = acid20rj_copy["Index_mes"].apply(lambda Index_mes: g(Index_mes))
print ("2020 ok")


# In[136]:


# Deletando colunas Index Mês para todas as bases

del infra17rj_copy['Index_mes'] 
del infra18rj_copy['Index_mes']
del infra19rj_copy['Index_mes']
del infra20rj_copy['Index_mes']

del acid17rj_copy['Index_mes']
del acid18rj_copy['Index_mes']
del acid19rj_copy['Index_mes']
del acid20rj_copy['Index_mes']


# ## Convertando Data para datetime

# In[138]:


#Convertendo coluna 'Data' de Infrações pra tipo datetime

infra17rj_copy['Data'] = infra17rj_copy.Data.astype('datetime64')
print ("Infra 2017 ok")
infra18rj_copy['Data'] = infra18rj_copy.Data.astype('datetime64')
print ("Infra 2018 ok")
infra19rj_copy['Data'] = infra19rj_copy.Data.astype('datetime64')
print ("Infra 2019 ok")
infra20rj_copy['Data'] = infra20rj_copy.Data.astype('datetime64')
print ("Infra 2020 ok")


# In[139]:


#Convertendo Data de Acidentes pra datetime

acid17rj_copy['Data'] = acid17rj_copy.Data.astype('datetime64')
print ("Acid 2017 ok")
acid18rj_copy['Data'] = acid18rj_copy.Data.astype('datetime64')
print ("Acid 2018 ok")
acid19rj_copy['Data'] = acid19rj_copy.Data.astype('datetime64')
print ("Acid 2019 ok")
acid20rj_copy['Data'] = acid20rj_copy.Data.astype('datetime64')
print ("Acid 2020 ok")


# ## Convertendo Ilesos, Feridos e Óbitos para inteiro

# In[141]:


# Converter Ilesos para inteiro

acid17rj_copy['Ilesos'] =  pd.to_numeric(acid17rj_copy['Ilesos'], errors="coerce").astype('int64')
print ("Conversão Acid 2017 ok")
acid18rj_copy['Ilesos'] =  pd.to_numeric(acid18rj_copy['Ilesos'], errors="coerce").astype('int64')
print ("Conversão Acid 2018 ok")
acid19rj_copy['Ilesos'] =  pd.to_numeric(acid19rj_copy['Ilesos'], errors="coerce").astype('int64')
print ("Conversão Acid 2019 ok")
acid20rj_copy['Ilesos'] =  pd.to_numeric(acid20rj_copy['Ilesos'], errors="coerce").astype('int64')
print ("Conversão Acid 2020 ok")


# In[142]:


# Converter Feridos_leves para inteiro

acid17rj_copy['Feridos_leves'] =  pd.to_numeric(acid17rj_copy['Feridos_leves'], errors="coerce").astype('int64')
print ("Conversão Acid 2017 ok")
acid18rj_copy['Feridos_leves'] =  pd.to_numeric(acid18rj_copy['Feridos_leves'], errors="coerce").astype('int64')
print ("Conversão Acid 2018 ok")
acid19rj_copy['Feridos_leves'] =  pd.to_numeric(acid19rj_copy['Feridos_leves'], errors="coerce").astype('int64')
print ("Conversão Acid 2019 ok")
acid20rj_copy['Feridos_leves'] =  pd.to_numeric(acid20rj_copy['Feridos_leves'], errors="coerce").astype('int64')
print ("Conversão Acid 2020 ok")


# In[143]:


# Converter Feridos_graves para inteiro

acid17rj_copy['Feridos_graves'] =  pd.to_numeric(acid17rj_copy['Feridos_graves'], errors="coerce").astype('int64')
print ("Conversão Acid 2017 ok")
acid18rj_copy['Feridos_graves'] =  pd.to_numeric(acid18rj_copy['Feridos_graves'], errors="coerce").astype('int64')
print ("Conversão Acid 2018 ok")
acid19rj_copy['Feridos_graves'] =  pd.to_numeric(acid19rj_copy['Feridos_graves'], errors="coerce").astype('int64')
print ("Conversão Acid 2019 ok")
acid20rj_copy['Feridos_graves'] =  pd.to_numeric(acid20rj_copy['Feridos_graves'], errors="coerce").astype('int64')
print ("Conversão Acid 2020 ok")


# In[144]:


# Converter Obitos para inteiro

acid17rj_copy['Obitos'] =  pd.to_numeric(acid17rj_copy['Obitos'], errors="coerce").astype('int64')
print ("Conversão Acid 2017 ok")
acid18rj_copy['Obitos'] =  pd.to_numeric(acid18rj_copy['Obitos'], errors="coerce").astype('int64')
print ("Conversão Acid 2018 ok")
acid19rj_copy['Obitos'] =  pd.to_numeric(acid19rj_copy['Obitos'], errors="coerce").astype('int64')
print ("Conversão Acid 2019 ok")
acid20rj_copy['Obitos'] =  pd.to_numeric(acid20rj_copy['Obitos'], errors="coerce").astype('int64')
print ("Conversão Acid 2020 ok")


# In[176]:


# Verificou-se todas as bases para garantir que estivessem com o mesmo type nas colunas
# Ex: infra20rj_copy2.info()


# # Agora vamos unir as planilhas de infrações e criar apenas uma geral para o estado de RJ

# In[152]:


#Verificou-se o shape de todos para garantir que estivessem com o mesmo shape
infra20rj_copy.shape


# In[150]:


# Agora que checamos tudo, podemos concatenar as bases
# Aqui concatenamos INFRACOES
infra_rj = pd.concat([infra17rj_copy, infra18rj_copy, infra19rj_copy, infra20rj_copy], join = 'inner')
print("Concatenação Infrações RJ concluída")


# In[147]:


# Concatenando ACIDENTES
acid_rj = pd.concat([acid17rj_copy, acid18rj_copy, acid19rj_copy, acid20rj_copy], join = 'inner')
print("Concatenação Acidentes RJ concluída")


# In[153]:


#Verificaremos o shape, para garantir que todas as linhas estão presentes
infra_rj.shape


# In[154]:


#Verificaremos o shape, para garantir que todas as linhas estão presentes
acid_rj.shape


# In[155]:


acid_rj.info()


# In[156]:


infra_rj.info()


# # Agora exportaremos essas bases para um arquivo

# In[148]:


# Exportação Acidentes RJ
acid_rj.to_excel(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Final\ACID_RJ_FIN.xlsx", index = False, header=True)
print("Exportação concluída")


# In[151]:


# Exportação Infrações RJ
infra_rj.to_csv(r"E:\CAMILA DRIVE\02.BIG_DATA_PUC\13.TCC\Final\INFRA_RJ_FIN.csv", sep = ',', index = False, header=True)
print("Exportação concluída")

