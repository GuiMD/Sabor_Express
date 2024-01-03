import os

restaurantes = ['Pizza', 'Sushi', 'Lasanha']   #Lista de restaurantes que serão cadastrados.

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opções():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')              #comando que limpa o Terminal
    print('APP Finalizado\n')

def opcao_invalida():
    print('Opção Inválida.\n')
    input('Digite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do novo restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input('\nDigite uma tecla para voltar ao Menu Principal ')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os Restaurantes\n')
    for restaurante in restaurantes:          #pra cada restaurante na lista, mostre o nome dele.
        print(f'.{restaurante}')
    input('\nDigite uma tecla para voltar ao Menu Principal ')
    main()

def escolher_opção():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        #Outra forma de tornar INT => opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:                    #Se colocarem um número errado no input.
            opcao_invalida()
    except:                      #Se não colocarem um número no input.
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opção()

if __name__ == '__main__':
    main()

