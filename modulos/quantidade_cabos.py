import numpy as np
from .funcoes_acessorias import verificar_existencia_arquivos, escrever_txt, ler_txt, apagar_arquivo 

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
        elif resposta == 3:
            menu_cabos('apagar')


def menu_cabos(parte_do_menu):
    endereco = './data/cabos.txt'
    match parte_do_menu:

        case 'verificar':
            verificador = verificar_existencia_arquivos(endereco)
            return verificador
        
        case 'registro_existente':
            print('\nJá existe registro de cabos!!!')
            resposta = int(input('''
[1] Novo Registro
[2] Ver o existente
[3] Apagar registro existente
-> '''))
            return resposta
        
        case 'novo_registro':
            print('\n','-'*10,'Registro de cabos','-'*10)
            try: 
                quantidade = int(input('Deseja inserir quantos cabos?: ').strip())
            except:
                return print('Quantidade inserida não é um valor!\n')
            
            dados_cabos = inserir_cabos(quantidade)
            if len(dados_cabos) > 0:
                escrever_txt(endereco,dados_cabos)

        case 'ver_existente':
            dados_cabos = ler_txt(endereco)
            print(dados_cabos)
        
        case 'editar':
            while True:    
                escolha_editar = int(input('Qual item você deseja editar?: '))
                dados_cabos = ler_txt(endereco)
                
                dados_cabos.loc[escolha_editar, 'Nome do Cabo'] = (str(input('Tipo de cabo: ')))
                dados_cabos.loc[escolha_editar, 'Quantidade(m)'] = (int(input('Quantidade do cabo: ')))
    

                continuar = input('Deseja Continuar?[S/N]').capitalize().strip()

                if continuar == 'N':
                    break     
        case 'apagar':
            apagar_arquivo('./data/cabos.txt')



def inserir_cabos(quantidade):
    cabos = np.zeros((quantidade+1, 2), dtype=object)
    cabos[0] = ['Nome do Cabo', 'Quantidade(m)']
    for cabo in range(1, quantidade+1):
        cont = 0
        while True:
            cont += 1

            print('')
            print(f'{cabo}º:')
        
            try: 
                cabos[cabo][0] = (str(input('Tipo de cabo: ').strip().capitalize()))
                cabos[cabo][1] = (int(input('Quantidade do cabo: ')))
            except:
                print('Erro na inserção de algum valor')
                if cont == 3:
                    break
            else:
                break
        if cont == 3:
            break
    if cont == 3:
        return ''
    else:
        return cabos        

