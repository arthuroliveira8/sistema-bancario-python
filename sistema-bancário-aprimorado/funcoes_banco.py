from pickle_files import *


def sacar(*, valor, contas, conta_atual):
    num_saques = contas[conta_atual][4]
    saldo = contas[conta_atual][2]

    if num_saques == 3:
        print("Não foi possível completar a operação. Limite de saques diário atingido (3).")
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    if valor > 500.00:
        print("Não foi possível completar a operação, pois o limite máximo de saque é de R$500.00.")
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    if valor < 0.01:
        print("O valor informado é inválido.")
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    if saldo < valor:
        print("Não foi possível completar a operação por falta de saldo.")
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    
    saldo -= valor
    contas[conta_atual][2] = saldo
    print(f"Seu novo saldo é de R${saldo:.2f}")
    contas[conta_atual][4] = num_saques + 1
    contas[conta_atual][3] += f"Saque: - R$ {valor:.2f}\n"
    writeContas(contas)
    input('Pressione qualquer tecla para continuar. ')
    os.system('cls')

def depositar(valor, contas, conta_atual):
    saldo = contas[conta_atual][2]
    if valor < 0.01:
        print("O valor informado é inválido.")
        return os.system('cls')
    
    saldo += valor
    contas[conta_atual][2] = saldo
    print(f"Seu novo saldo é de R${saldo:.2f}")
    contas[conta_atual][3] += f"Depósito: + R$ {valor:.2f}\n"
    writeContas(contas)
    input('Pressione qualquer tecla para continuar.')
    os.system('cls')
    
def visualizar_extrato(contas, conta_atual): # TODO: transformar extrato em uma só string contendo depósitos e saques
    saldo = contas[conta_atual][2]
    extrato = contas[conta_atual][3]
    print('========== EXTRATO ==========')
    print('Nenhuma movimentação foi registrada na sua conta.\n\n' if not extrato else extrato) 
    print(f"Seu saldo atual é de R${saldo:.2f}\n")
    input('Pressione qualquer tecla para continuar.')
    os.system('cls')


def cadastrar_usuario(usuarios):
    cpf = pegar_cpf()
    for i in usuarios:
            if cpf in i.values(): #TODO: TypeError: argument of type 'builtin_function_or_method' is not iterable
                print('Usuário já cadastrado. Tente novamente.')
                input('Pressione qualquer tecla para continuar.')
                return os.system('cls')
    if isinstance(cpf, str):
        print('Tente novamente.')
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    usuario = input('Insira seu nome completo: ')
    data_nasc = input('Insira sua data de nascimento (XX-XX-XXXX): ')
    if not any(char.isalpha() for char in data_nasc):
        pass
    else:
        print('Por favor, insira apenas números.')
        input("Pressione qualquer tecla para continuar.")
        return os.system('cls')
    if len(data_nasc) == 10:
        pass
    else:
        print('Data de nascimento inválida, tente novamente.')
        input("Pressione qualquer tecla para continuar.")
        return os.system('cls')
    endereço = input('Insira o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome':usuario, 'cpf':cpf, 'data_nasc':data_nasc, 'endereço':endereço})
    writeUsuarios(usuarios)

    print('Usuário registrado com sucesso!')
    input("Pressione qualquer tecla para continuar.")
    os.system('cls')

def pegar_cpf():
    try:
        cpf = int(input("Informe o seu CPF (somente números): "))
    except ValueError:
        print('Por favor, insira apenas números.', end=' ')
        return 'sair'
    if len(str(cpf)) == 11:
        return cpf
    else: 
        print('Número inválido.')
        return 'sair'

def criar_conta(usuarios, contas):
    cpf = pegar_cpf()
    if isinstance(cpf, str):
        print('Tente novamente.')
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    senha = int(input('Digite a senha da sua nova conta(somente números inteiros): '))
    if not usuarios:
        print('Não há usuários registrados no sistema. Tente novamente.')
        input('Pressione qualquer tecla para continuar.')
        return os.system('cls')
    for i in usuarios:
        if cpf in i.values():
            nome = i['nome']
            break
        else:
            print('Este CPF não está registrado no sistema. Tente novamente.')
            input('Pressione qualquer tecla para continuar.')
            return os.system('cls')
    input(contas)
    if not contas.keys():
        num = 1
    else:    
        num = max(contas.keys()) + 1
    contas[num] = [nome, senha, 0, '', 0] #4 = num saques
    writeContas(contas)
    print(f'Conta criada com sucesso! O número da sua conta é 0001-{num}')
    input("Pressione qualquer tecla para continuar.")
    return os.system('cls')

def login(contas): #TODO: adicionar uma checagem do numero da agencia e do hifen
    conta = input('Informe sua conta utilizando o formato XXXX-X: ')
    if conta[:5] != '0001-':
        input('Número de conta e/ou senha inválido(s)! Pressione qualquer tecla para continuar.')
        os.system('cls')
        return False
    conta = int(conta[5:])
    senha = int(input('Informe sua senha: '))
    if conta in contas.keys(): #TODO: criar um dic com as contas ={conta: [nome, senha, saldo, extrato]}
        if senha in contas[conta]:
            input('Login realizado com sucesso! Pressione qualquer tecla para continuar.')
            os.system('cls')
            return conta
        else:
            input('Número de conta e/ou senha inválido(s)! Pressione qualquer tecla para continuar.')
            os.system('cls')
            return False
    else:
        input('Número de conta e/ou senha inválido(s)! Pressione qualquer tecla para continuar.')
        os.system('cls')
        return False

def remover_conta(contas, conta_atual):
    confi = input('Tem certeza que deseja excluir a conta? ("S" para Sim e "N" para Não): ')
    if confi.upper() == 'S':
        contas.pop(conta_atual)
        writeContas(contas)
        input(f'Conta {conta_atual} foi deletada com sucesso! Pressione qualquer tecla para continuar')
        conta_atual = 0
    elif confi.upper() == 'N':
        return os.system('cls')
    else:
        print("Por favor, utilize apenas S ou N para responder a pergunta. Tente novamente.")
        input('Pressione qualquer tecla para continuar')
        return os.system('cls')

def remover_usuario(conta_atual, contas, usuarios): # TODO: adicionar mensagem de confirmação, lembrar de deletar todas as contas daquele usuário.
    pop = []
    confi = input('Tem certeza que deseja excluir o usuário e todas as contas associadas a ele? ("S" para Sim e "N" para Não): ')
    if confi.upper() == 'S':
        titular = contas[conta_atual][0]
        for i, j in contas.items(): #deleta todas as contas associadas a aquele usuário
            if titular in j: 
                pop.append(i)

        for i in pop:
            del contas[i]
        
        atual = 0
        for i in usuarios: # deleta o usuário
            if titular in i.values():
                del usuarios[atual]
                break
            atual +=1
        
        writeContas(contas), writeUsuarios(usuarios)
        input(f'Usuário {titular} foi deletado com sucesso! Pressione qualquer tecla para continuar. ')
        conta_atual = 0
        return os.system('cls')
        
    elif confi.upper() == 'N':
        return os.system('cls')
    else:
        input("Por favor, utilize apenas S ou N para responder a pergunta. Tente novamente.\nPressione qualquer tecla para continuar.")
        return os.system('cls')