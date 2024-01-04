import os

restaurantes = [{'nome':'Sushi', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizzaria', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Feijoada', 'categoria':'Brasileira', 'ativo':False}]

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

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao Menu Principal ')
    main()

def opcao_invalida():
    print('Opção Inválida.\n')

    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do novo restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")

    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    print('Listando os Restaurantes\n')
    print(f'* {'Nome do Restaurante'.ljust(20)} * {'Categoria'.ljust(20)} * {'Status'}')
    for restaurante in restaurantes:          
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'| {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    os.system('cls')
    print('Ativando ou Desativando um Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:   #ver se existe no dicionário elemento igual.
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']   #not irá inverter o estado que está.
            if restaurante['ativo']:  #True
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'  
            else:  #False
                mensagem = f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Este nome de restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opção():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        #Outra forma de tornar INT => opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
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

