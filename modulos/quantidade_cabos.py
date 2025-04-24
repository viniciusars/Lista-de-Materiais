import numpy as np
from funcoes_acessorias import escrever_txt

def cabos():
    quantidade = int(input('Deseja inserir quantos cabos?: '))
    cabos = inserir_cabos(quantidade)
    escrever_txt('./data/cabos.txt',cabos)    

def inserir_cabos(quantidade):
    cabos = np.zeros((quantidade+1, 2), dtype=object)
    cabos[0] = ['Nome do Cabo', 'Quantidade(m)']
    for cabo in range(1, quantidade+1):
        cabos[cabo][0] = (str(input('Tipo de cabo: ')))
        cabos[cabo][1] = (input('Quantidade do cabo: '))
    return cabos

if __name__=="__main__":
    cabos()
    