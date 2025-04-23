import numpy as np
from funcoes_acessorias import verificar_existencia_arquivos, escrever_txt, ler_txt 

def cabos():
    verificador = menu_cabos('verificar')
    if not verificador:
        menu_cabos('novo_registro')
    else:
        resposta = menu_cabos('registro_existente')
        if resposta == 1:
            menu_cabos('novo_registro')
        elif resposta == 2:
            menu_cabos('ver_existente')
            menu_cabos('editar')


def menu_cabos(parte_do_menu):
    endereco = './data/cabos.txt'
    match parte_do_menu:

        case 'verificar':
            verificador = verificar_existencia_arquivos(endereco)
            return verificador
        
        case 'registro_existente':
            print('Já existe registro de cabos!!!\n')
            resposta = int(input('''
[1] Novo Registro
[2] Ver o existente
-> '''))
            return resposta
        
        case 'novo_registro':
            quantidade = int(input('Deseja inserir quantos cabos?: ').strip())
            dados_cabos = inserir_cabos(quantidade)
            escrever_txt(endereco,dados_cabos)

        case 'ver_existente':
            dados_cabos = ler_txt(endereco)
            print(dados_cabos)
        
        case 'editar':
            while True:    
                escolha_editar = int(input('Qual item você deseja editar?: '))
                dados_cabos = ler_txt(endereco)
                
                dados_cabos.loc[escolha_editar, 'Nome do Cabo'] = (str(input('Tipo de cabo: ')))
                dados_cabos.loc[escolha_editar, 'Quantidade(m)'] = (input('Quantidade do cabo: '))

                continuar = input('Deseja Continuar?[S/N]').capitalize().strip()

                if continuar == 'N':
                    break                    




def inserir_cabos(quantidade):
    cabos = np.zeros((quantidade+1, 2), dtype=object)
    cabos[0] = ['Nome do Cabo', 'Quantidade(m)']
    for cabo in range(1, quantidade+1):
        cabos[cabo][0] = (str(input('Tipo de cabo: ')))
        cabos[cabo][1] = (input('Quantidade do cabo: '))
    return cabos        


if __name__=="__main__":
    cabos()

