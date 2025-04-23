from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import pandas as pd

def local(titulo='Selecione um arquivo'):
    root = Tk()
    root.withdraw()
    caminho = askopenfilename(title= titulo)
    root.destroy()
    return caminho

def diretorio():
    caminho = os.getcwd()
    caminho = caminho.replace("\\","/")
    return caminho

def verificar_existencia_arquivos(caminho):
    if os.path.exists(caminho):
        return True
    else:
        return False

def local_de_salvar(nome_do_arquivo):
    caminho_final = diretorio() + '/' + nome_do_arquivo
    return caminho_final

#! Função para salvar a tabela de locação num csv
def escrever_csv(caminho, dados): 
    with open(caminho, 'w') as f: # Recebe o local onda vai ser salvo e que vai escrever nesse arquivo
        for row in dados: # Dados vai ser uma lista com listas dentro e cada lista representa uma linha da tabela de locação
            cont = 1
            '''
            No código antigo, depois de todo valor da lista era inserida uma vírgula e,
            quando ia pegar essa arquivo para consulta, uma nova coluna com nenhum valor
            aparecia justamente por todo valor ser acompanhado por uma vírgulo. Por isso
            foi inserido esse contador para que o último valor da linha não seja acompanhado
            com a vírgulo e não ter essa coluna vazia extra
            '''
            for item in row: # Outro for com cada item da linha da tabela de locação
                '''
                Existe um problema com os elementos que são números e, principalmente float.
                As casas decimais desses números crescem muito e o método open() só consegue
                escrever valores que são str. Para resolver isso, arredonda os valores que 
                são float e transforma tudos os valores para str.
                '''
                if isinstance(item, float): 
                    item = round(item, 2)
                
                '''
                O último ponto de verificação é o da última vírgula. Depois de todo valor é adicionada uma 
                vírgulo, pois é um arquivo csv. Porém, não deve ser inserida essa vírgulo no último elemento, 
                pois, se isso acontecer, o arquivo entenderá que existe uma coluna extra que na realidade não
                existe.
                '''
                if cont != len(row):
                    if item is None:
                        f.write(" "+",")
                    else:
                        f.write(str(item)+",")
                else:
                    f.write(str(item))
                cont = cont + 1
            f.write("\n") # No final de cada linha da tabela de locação, dá uma quebra de linha

def escrever_txt(caminho, variavel):
    with open(caminho, "w") as f:
        for linha in range(0, len(variavel)):
            for coluna in range(0, len(variavel[0])):
                f.write(f"{variavel[linha][coluna]}")
                if coluna < len(variavel[0])-1:   
                    f.write(',')
            f.write("\n")

def ler_txt(caminho):
    conteudo = []
    with open(caminho, "r") as f:
        for line in f.readlines():
            line = line.replace('\n','').split(',')
            conteudo.append(line)
    conteudo = pd.DataFrame(conteudo[1:], columns=conteudo[0])
    return conteudo

if __name__ == '__main__':
    conteudo = ler_txt('./data/cabos.txt')
    