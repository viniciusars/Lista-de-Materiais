import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os
import tkinter as tk
from tkinter import filedialog


def local(mensagem):
    root = tk.Tk()
    root.withdraw()

    caminho = filedialog.askopenfilename(title= mensagem)
    return caminho



def quant_postes():
    dados = [['Número','Vértice','Deflexão','Tipo','Altura/carga','Posição','Vão de frente','Distância progressiva','Nível 1','Circuito', 'Nível 2', 'Circuito', 'Âncora', 'Estais']]
    caminho=local('Selecione a tabela de locação')
    wb = load_workbook(caminho)
    for sheets in wb.sheetnames:
        if "TABELA DE LOCAÇÃO" in sheets:
            for row in wb[sheets].iter_rows(min_row=8,max_row=82, min_col=1, max_col=14, values_only=True):
                    valores_nulos = 0
                    for x, elemento in enumerate(row):
                        if elemento is None:
                            valores_nulos = valores_nulos + 1
                    if valores_nulos < 14:
                        dados.append(row)
    caminho_pasta = "/".join(caminho.split("/")[:-1])
    caminho_pasta = caminho_pasta + "/infos.txt"
    
    with open(caminho_pasta, "w") as f:
         for row in dados:
            for item in row:
                if isinstance(item, float):
                    item = round(item, 2)
                if item is None:
                    f.write(" "+";")
                else:
                    f.write(str(item)+";")
            f.write("\n")
   

quant_postes()
