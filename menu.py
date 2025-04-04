import func
def menu():
    while True:
        print('\n--------','LISTA DE MATERIAIS','--------')
        mensagem_menu()
        resposta = int(input('Escolha a opção: '))
        escolha(resposta)

def mensagem_menu():
    print('[1] - Escolher a Tabela de Locação\n' \
    '[2] - Contabilizar as materiais padrão\n' \
    '[3] - Contabilizar os parafusos\n' \
    '[4] - Salvar arquivos\n' \
    '[0] - Encerrar\n')

def escolha(resposta):
    match resposta:
        case int(1):
            func.pegar_postes()
        case 2:
            func.quant_postes()
        case 3:
            print('Ainda não está pronto')
        case 4:
            print('Ainda não está pronto')
        case 0:
            return False
        case _:
            print('Opção inválida!')

menu()

