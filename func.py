import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def local(mensagem):
    root = tk.Tk()
    root.withdraw()

    caminho = filedialog.askopenfilename(title= mensagem)
    return caminho

def pegar_postes():
    '''
    Lista que vai receber todos os as linhas válidas da tabela de locação
    Esses valores pré-definidos compõe o cabeçalho
    '''
    dados = [['Número','Vértice','Deflexão','Tipo','Altura/carga','Posição','Vão de frente','Distância progressiva','Nível 1','Circuito 1', 'Nível 2', 'Circuito 2', 'Âncora', 'Estais']]
    
    # Pegar o caminho do arquivo da tabela de locação que vai ser utilizada
    caminho=local('Selecione a tabela de locação')
    
    # Carrega o documento como um workbook pela biblioteca openpyxl
    wb = load_workbook(caminho)

    '''
    Esse FOR vai pegar todos os valores válidos para esse caso em particular.
    No documento selecionado, há outras abas que não possuem valores de interesse, dessa forma,
    só vamos localizar os valores que estão nas abas com o nome TABELA DE LOCAÇÃO 
    '''
    for sheets in wb.sheetnames: # Percorre o nome de todas as worksheets (abas da planilha)
        if "TABELA DE LOCAÇÃO" in sheets: # Verifica se, no nome da aba, possue o texto TABELA DE LOCAÇÃO (abas do nosso interesse)
            # Esse for vai iterar sobre todas as linhas das abas selecionadas
            for row in wb[sheets].iter_rows(min_row=8,  # Primeira linha dessa iteração
                                            max_row=82, # última linha 
                                            min_col=1,  # Primeira coluna
                                            max_col=14, # última coluna
                                            values_only=True # Pegar os valores de dentro da célula, se remover, ele pega a referência da célula
                                            ):
                    '''
                    O trecho a seguir verifica quantos elementos não possuem valores (None), se a linha toda for None,
                    essa linha não será adicionada a lista DADOS. Como 14 colunas são colhidas (14 valores), o for a seguir
                    itera sobre esses 14 valores verificando se são None, caso todos forem, essa linha não vai ser inserida
                    '''
                    valores_nulos = 0
                    for x, elemento in enumerate(row):
                        if elemento is None:
                            valores_nulos = valores_nulos + 1
                    if valores_nulos < 14:
                        dados.append(row)

    # No pensamento atual, faço a obtenção de todos esses valores e jogo para um arquivo .txt
    caminho_pasta = "/".join(caminho.split("/")[:-1])
    caminho_pasta = caminho_pasta + "/infos.csv" #Obtenção do caminho que esse arquivo será gerado e salvo 
    
    # For para escrever todos os valores presentes na lista DADOS
    with open(caminho_pasta, "w") as f:
         for row in dados:
            for item in row:
                if isinstance(item, float): # Esse método não aceita float para escrever, tem que transformar em str
                    item = round(item, 2)
                if item is None: # Esse método também não aceita valores None, então tranforma-se em " "
                    f.write(" "+",")
                else:
                    f.write(str(item)+",")
            f.write("\n")

def quant_postes():
    caminho = os.getcwd()
    caminho = caminho.replace("\\","/") + "/infos.csv"
    postes = pd.read_csv(caminho, encoding= 'latin-1')
    postes.drop(postes.columns[[14]], axis=1, inplace= True)
    postes_unicos = postes['Tipo'].value_counts().reset_index()

    caminho_planilha_descricao_postes = os.getcwd()
    caminho_planilha_descricao_postes = caminho_planilha_descricao_postes.replace('\\','/') + '/POSTES.xlsx'
    wb = load_workbook(caminho_planilha_descricao_postes)

    colunas = []
    indice = []
    for sheet in wb.sheetnames:
        for row in wb[sheet].iter_rows(min_row=2, max_col=2, min_col=2, values_only=True):
            indice.append(row)
        if 'N4_N3.TR_CH' in sheet:
            sheet = sheet.replace('N4_N3.TR_CH','N4/N3.TR-CH')
        elif 'N4_N4.TR_CH' in sheet:
            sheet = sheet.replace('N4_N4.TR_CH','N4/N4.TR-CH')
        else:
            sheet = sheet.replace('_','-')
        colunas.append(sheet)

    indice = pd.DataFrame(indice)
    indice = indice[0].sort_values(ascending=True).unique()
    
    df_planilha_descricao_postes = pd.DataFrame(index= indice, columns=colunas)
    
    print(df_planilha_descricao_postes)

quant_postes()