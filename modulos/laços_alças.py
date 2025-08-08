import pandas as pd
from .funcoes_acessorias import ler_txt
import numpy as np

def tabela_com_valores_cabo_alca_estrutura():
    tabela_consulta = pd.read_csv('./data/alcas_lacos.csv', header=[0,1,2], sep=';').dropna()
    return tabela_consulta

def tabela_de_locacao():
    tabela_locacao= pd.read_csv('./data/tabela_de_locacao.csv', encoding='latin-1')
    return tabela_locacao

def quantidade_estrutura_por_cabo():

    # indice_tabela = tabela_locacao['Tipo'].unique()
    indice = indice_quantidade_estrutura_por_cabo()
    colunas = coluna_quantidade_estrutura_por_cabo()
    tabela = pd.DataFrame(index= indice, columns= colunas)
    
    

def quantidade_de_niveis():
    tabela = tabela_de_locacao()
    count = 0
    for c in tabela.columns:
        if 'Nível' in c:
            count = count + 1
    return count

def tipos_cabos():
    tabela = tabela_de_locacao()
    niveis = quantidade_de_niveis()
    cabos = []
    for c in range(1, niveis+1):
        for linha in tabela.index:
            cabos.append(tabela.loc[linha, (f'Nível {c}')])
    cabos = pd.Series(cabos).unique()
    return cabos

def coluna_quantidade_estrutura_por_cabo():
    niveis = quantidade_de_niveis()
    cabos = tipos_cabos()
    colunas = []

    for x in range(1, niveis+1):
        for y,cabo in enumerate(cabos):
            colunas.append(((f'Nível {x}'),('VANTE'),(cabo)))
            colunas.append(((f'Nível {x}'),('RÉ'),(cabo)))
    colunas = pd.MultiIndex.from_tuples(colunas)
    return colunas

def indice_quantidade_estrutura_por_cabo():
    tabela = tabela_de_locacao()
    estruturas = []
    
    for index in tabela.index:
        estruturas.append(tabela.loc[index, 'Tipo'])

    estruturas = pd.Series(estruturas).unique()
    return estruturas

def tabela_de_locacao_re_vante():
    tabela = tabela_de_locacao()
    niveis = quantidade_de_niveis()
    indices = indice_quantidade_estrutura_por_cabo()
    colunas = coluna_quantidade_estrutura_por_cabo()
    cabos = tipos_cabos()

    planilha = pd.DataFrame(columns= colunas, index= indices)

    for indice in planilha.index:
        for nivel in range(1, niveis+1):
            for cabo in cabos:
               planilha.loc[indice,[(f'Nível {nivel}', 'VANTE', cabo)]] = tabela[[(f'Nível {nivel}'), 'Tipo']].value_counts().get((indice, cabo), 0)
    #! CONTINUAR DAQUIIIIIIIIIIIIIIIIIIIIIIIIIIIII