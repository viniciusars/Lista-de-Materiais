from quantidade_total import gerar_df_info_postes
from tabela_de_locacao import pegar_postes
from funcoes_acessorias import verificar_existencia_arquivos

def menu():
    while True:
        print('\n--------','LISTA DE MATERIAIS','--------')
        mensagem_menu()
        resposta = int(input('Escolha a opção: '))
        continuar = escolha(resposta)
        if not continuar:
            break

def mensagem_menu():
    print('[1] - Escolher a Tabela de Locação\n' \
    '[2] - Contabilizar as materiais padrão\n' \
    '[3] - Contabilizar os parafusos\n' \
    '[4] - Salvar arquivos\n' \
    '[0] - Encerrar\n')

def escolha(resposta):
    match resposta:
        case 1:
            pegar_postes()
        case 2:
            verificador = verificar_existencia_arquivos('./data/Tabela_de_Locacao.csv')
            if verificador:
                resultado = gerar_df_info_postes()
                print(resultado)
            else:
                print('''
Ainda não foi escolhida nenhuma tabela de locação
Faça a opção 1 para dar prosseguimento!!!
                      ''')
        case 3:
            print('Ainda não está pronto')
        case 4:
            print('Ainda não está pronto')
        case 0:
            print('Encerrando Programa!!!')
            return False
        case _:
            print('Opção inválida!')
    return True

if __name__ == "__main__":
    menu()
