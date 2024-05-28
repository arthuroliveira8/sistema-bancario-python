from funcoes_banco import *

sair = False
conta_atual = 0

try:
    contas, usuarios = readContas(contas), readUsuarios(usuarios)
except FileNotFoundError:
    writeContas(contas), writeUsuarios(usuarios)
    contas, usuarios = readContas(contas), readUsuarios(usuarios)

while sair == False:
    voltar = False
    while True:
        strt = input('''\nBem-vindo(a). Faça login com uma conta e senha ou crie sua conta.\n
        Caso seja novo, lembre-se de cadastrar um novo usuário.\n
        Utilize "S" para finalizar.\n
        1. Login\n
        2. Nova Conta\n
        3. Novo Usuário\n
        S. Sair\n
        >>> ''')

        if strt == '1':
            entrada = login(contas)
            if not isinstance(entrada, bool):
                conta_atual = entrada
                break
            else:
                pass
        elif strt == '2':
            criar_conta(usuarios, contas)
        elif strt == '3':
            cadastrar_usuario(usuarios)
        elif strt.upper() == 'S':
            os.system('clear')
            sair = True
            break
        else:
            print('Operação inválida! Tente novamente.')
            input("Pressione qualquer tecla para continuar.")
            os.system('clear')

    while sair == False and voltar == False:   #Adicionar nesse segundo menu uma janela com as informações do titular.
        op = input('''\nEscolha a operação que deseja realizar. Utilize "S" para voltar para tela de login.\n
        1. Sacar\n
        2. Depositar\n
        3. Extrato\n
        4. Excluir Conta\n
        5. Excluir Usuário\n
        S. Voltar\n
        >>> ''')

        if op == '1': # Sacar
            valor = float(input("Qual o valor que deseja sacar?\n>>> "))
            sacar(valor=valor, contas=contas, conta_atual=conta_atual)
        elif op == '2': # Depósito
            valor = float(input("Qual o valor que deseja depositar?\n>>> "))
            depositar(valor, contas, conta_atual)
        elif op == '3': # Extrato
            visualizar_extrato(contas, conta_atual)
        elif op == '4':
            remover_conta(contas, conta_atual)
            os.system('clear')
            voltar = True
        elif op == '5':
            remover_usuario(conta_atual, contas, usuarios)
            voltar = True
        elif op.upper() == 'S':
            os.system('clear')
            voltar = True
        else:
            print("Operação inválida! Tente novamente.")
            input("Pressione qualquer tecla para continuar.")
            os.system('clear')