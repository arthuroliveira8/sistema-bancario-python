import os

def sacar(valor):
    global saldo
    global num_saques

    if num_saques == 3:
        print("Não foi possível completar a operação. Limite de saques diário atingido (3).")
        return
    if valor > 500.00:
        print("Não foi possível completar a operação, pois o limite máximo de saque é de R$500.00.")
        return
    if valor < 0.01:
        print("O valor informado é inválido.")
        return
    if saldo < valor:
        print("Não foi possível completar a operação por falta de saldo.")
        return
    
    saldo -= valor
    print(f"Seu novo saldo é de R${saldo:.2f}")
    num_saques += 1
    saques.append(valor)

def extrato():
    tdep, tsaq = 0, 0 #total depósito, total saque
    if not(depositos or saques):
        print("Não foram realizadas movimentações.")
        return
    
    print("DEPÓSITOS".center(18, "-"))
    for i in depositos:
        print(f"  + R${i:.2f}\n")
        tdep += i
    print(f"TOTAL: + R${tdep:.2f}")
    print()

    print("SAQUES".center(18, "-"))
    for i in saques:
        print(f"  - R${i:.2f}\n")
        tsaq += i
    print(f"TOTAL: - R${tsaq:.2f}")
    print()
    
    print(f"Seu saldo atual é de R${saldo:.2f}")

def depositar(valor):
    global saldo
    if valor < 0.01:
        print("O valor informado é inválido.")
        return
    
    saldo += valor
    print(f"Seu novo saldo é de R${saldo:.2f}")
    depositos.append(valor)

saldo = 0
num_saques = 0
num_deps = 0
depositos, saques = [], []

while True:
    op = input('Bem-vindo(a). Escolha a operação que deseja realizar. Utilize "S" para finalizar.\n1. Sacar\n2. Depositar\n3. Extrato\nS. Sair\n>>> ')

    if op == '1': # Sacar
        valor = float(input("Qual o valor que deseja sacar?\n>>> "))
        sacar(valor)
    elif op == '2': # Depósito
        valor = float(input("Qual o valor que deseja depositar?\n>>> "))
        depositar(valor)
    elif op == '3': # Extrato
        extrato()
    elif op.upper() == 'S': # Sair
        os.system('clear')
        break
    else:
        print("Operação inválida! Tente novamente.")


    input("Pressione qualquer tecla para continuar.")
    os.system('clear')
