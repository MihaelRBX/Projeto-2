# Pedro Henrique Mansano Fernandes - 42303885
# Mihael Rommel Barbosa Xavier - 32307861
# David Wei Bo Pan - 32330138

import random
import getpass
import os

cadastro_realizado = False
lista_de_operacoes = [[], []]
saldo = 0
TENTATIVA_SENHA = 3


def cadastrar_conta_corrente():
    global cadastro_realizado
    global numero_conta
    global nome_cliente
    global senha
    global saldo_inicial
    global saldo
    global limite_credito

    if cadastro_realizado:
        print('Você já realizou o cadastro uma vez. Não é permitido cadastrar mais de uma vez.\n')
        return

    print('MACK BANK - CADASTRO DE CONTA')

    numero_conta = 1234  # random.randint(1000, 9999)
    print('NÚMERO DA CONTA: ', numero_conta)

    nome_cliente = input('NOME DO CLIENTE: ').title()
    while not nome_cliente:
        print('Nome do cliente não pode estar em branco.')
        nome_cliente = input('NOME DO CLIENTE: ').title()

    telefone_cliente = input('TELEFONE.......: ')
    while not telefone_cliente:
        print('Telefone não pode estar em branco.')
        telefone_cliente = input('TELEFONE.......: ')

    email_cliente = input('EMAIL..........: ')
    while not email_cliente:
        print('Email não pode estar em branco.')
        email_cliente = input('EMAIL..........: ')

    saldo_inicial = float(input('SALDO INICIAL...:R$ '))
    while saldo_inicial < 1000:
        print('O saldo inicial deve ser maior ou igual a R$1000.')
        saldo_inicial = float(input('SALDO INICIAL...:R$ '))
    saldo = saldo_inicial
    limite_credito = float(input('LIMITE DE CRÉDITO: R$ '))
    while limite_credito < 0:
        print('O limite de crédito não pode ser menor que 0.')
        limite_credito = float(input('LIMITE DE CRÉDITO: R$ '))

    senha = getpass.getpass('SENHA..........: ')
    while len(senha) != 6:
        print('A SENHA DEVE SER COMPOSTA POR 6 CARACTERES.')
        senha = getpass.getpass('SENHA..........: ')

    confirmacao_senha = getpass.getpass('REPITA A SENHA...: ')
    while confirmacao_senha != senha:
        print('AS SENHAS INSERIDAS NÃO SÃO IGUAIS.')
        confirmacao_senha = getpass.getpass('REPITA A SENHA...: ')

    cadastro_realizado = True

    input('CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')


def depositar():
    global saldo
    print('MACK BANK - DEPÓSITO EN CONTA')
    depositar_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    while depositar_conta != numero_conta:
        print('NÚMERO INVÁLIDO. Por favor, tente novamente.')
        depositar_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    print(f'NOME DO CLIENTE: {nome_cliente}')
    valor_deposito = float(input('VALOR DO DEPÓSITO: R$'))
    while valor_deposito <= 0:
        print('O valor do depósito deve ser maior que R$ 0,00! Por favor, insira um valór válido. ')
        valor_deposito = float(input('VALOR DO DEPÓSITO: R$'))
    lista_de_operacoes[0].append(valor_deposito)
    if saldo == saldo_inicial:
        saldo += valor_deposito
    else:
        saldo += valor_deposito + saldo_inicial
    print('DEPÓSITO REALIZADO COM SUCESSO!\n')


def sacar():
    global TENTATIVA_SENHA
    global saldo
    global limite_credito
    print('MACK BANK - SAQUE')

    saque_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    while saque_conta != numero_conta:
        print('NÚMERO INVÁLIDO. Por favor, tente novamente.')
        saque_conta = int(input('INFORME O NÚMERO DA CONTA: '))

    print(f'NOME DO CLIENTE: {nome_cliente}')

    saque_senha = getpass.getpass('INFORME A SENHA: ')
    while saque_senha != senha:
        TENTATIVA_SENHA -= 1
        print(f'SENHA INCORRETA! Você tem mais {TENTATIVA_SENHA} chances.')
        if TENTATIVA_SENHA == 0:
            print("OPERAÇÃO BLOQUEDA!")
            return
        saque_senha = getpass.getpass('INFORME A SENHA: ')
    TENTATIVA_SENHA = 3
    valor_saque = float(input('VALOR DO SAQUE: R$'))
    while valor_saque <= 0:
        print('O valor do saque deve ser maior que R$ 0,00! Por favor, insira um valór válido. ')
        valor_saque = float(input('VALOR DO SAQUE: R$'))
    if valor_saque <= saldo:
        saldo -= valor_saque
    elif valor_saque <= saldo + limite_credito:
        print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
        if saldo:
            saque_credito = valor_saque - saldo
            saldo = 0
            limite_credito -= saque_credito
        else:
            limite_credito -= valor_saque
    else:
        print('SALDO INSUFICIENTE NA CONTA.')
    lista_de_operacoes[1].append(valor_saque)


def consultar_saldo():
    print('MACK BANK - CONSULTA SALDO')
    saldo_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    while saldo_conta != numero_conta:
        print('NÚMERO INVÁLIDO. Por favor, tente novamente.')
        saldo_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    print(f'NOME DO CLIENTE: {nome_cliente}')
    saldo_senha = getpass.getpass('INFORME A SENHA: ')
    while saldo_senha != senha:
        TENTATIVA_SENHA -= 1
        print(f'SENHA INCORRETA! Você tem mais {TENTATIVA_SENHA} chances.')
        if TENTATIVA_SENHA == 0:
            print("OPERAÇÃO BLOQUEDA!")
            return
        saldo_senha = getpass.getpass('INFORME A SENHA: ')
    TENTATIVA_SENHA = 3
    print('SENHA INCORRETA! Tente novamente.')
    saldo_senha = getpass.getpass('INFORME A SENHA: ')
    print(f'SALDO EM CONTA: R${saldo:,.2f}')
    print(f'LIMITE DE CRÉDITO: R${limite_credito:,.2f}')
    input('CADASTRO REALIZADO! CONFIRME UMA TECLA PARA VOLTAR AO MENU...')


def consultar_extrato():
    print('MACK BANK - EXTRADO DA CONTA')
    extrato_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    while extrato_conta != numero_conta:
        print('NÚMERO INVÁLIDO. Por favor, tente novamente.')
        extrato_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    print(f'NOME DO CLIENTE: {nome_cliente}')
    extrato_senha = getpass.getpass('INFORME A SENHA: ')
    while extrato_senha != senha:
        TENTATIVA_SENHA -= 1
        print(f'SENHA INCORRETA! Você tem mais {TENTATIVA_SENHA} chances.')
        if TENTATIVA_SENHA == 0:
            print("OPERAÇÃO BLOQUEDA!")
            return
        extrato_senha = getpass.getpass('INFORME A SENHA: ')
    TENTATIVA_SENHA = 3
    print(f'LIMITE DE CRÉDITO: R${limite_credito:,.2f}')
    print('ÚLTIMAS OPERAÇÕES:')


def imprimeEscolhas():
    print('MACK BANK - ESCOLHA UMA OPCÃO')
    print('   (1)   CADASTRAR CONTA CORRENTE')
    print('   (2)   DEPOSITAR')
    print('   (3)   SACAR')
    print('   (4)   CONSULTAR SALDO')
    print('   (5)   CONSULTAR EXTRATO')
    print('   (6)   FINALIZAR')


def finalizar():
    print('Você escolheu a opção para finalizar o programa.\n')
    print('MACK BANK - SOBRE')
    print('Este programa foi desenvolvido por:')
    print('Mihael Rommel Barbosa Xavier - 32307861')
    print('Pedro Henrique Mansano Fernandes - 42303885')
    print('David Wei Bo Pan - 32330138')

    # Lógica do programa


while True:
    # MENU
    imprimeEscolhas()
    opcao = int(input('SUA OPCÃO: '))
    while opcao < 1 or opcao > 6:
        opcao = int(input('OPCÃO INVÁLIDA, INSIRA UMA OPCAO VÁLIDA: '))

    # CADASTRO DA CONTA
    if opcao == 1:
        os.system('cls')
        cadastrar_conta_corrente()

    # DEPOSITAR
    elif opcao == 2:
        os.system('cls')
        if cadastro_realizado:
            depositar()
        else:
            print('Realize o cadastro da conta primeiro.')

    # SACAR
    elif opcao == 3:
        os.system('cls')
        if cadastro_realizado:
            if TENTATIVA_SENHA:
                sacar()
            else:
                print('OPERAÇÃO BLOQUEDA!')
        else:
            print('Realize o cadastro da conta primeiro.')

    # CONSULTAR SALDO
    elif opcao == 4:
        os.system('cls')
        if cadastro_realizado:
            if TENTATIVA_SENHA:
                consultar_saldo()
            else:
                print('OPERAÇÃO BLOQUEDA!')
        else:
            print('Realize o cadastro da conta primeiro.')

    # CONSULTA EXTRATO
    elif opcao == 5:
        os.system('cls')
        if cadastro_realizado:
            if TENTATIVA_SENHA:
                consultar_extrato()
            else:
                print('OPERAÇÃO BLOQUEDA!')
        else:
            print('Realize o cadastro da conta primeiro.')

    # FINALIZAR
    elif opcao == 6:
        finalizar()
        print(lista_de_operacoes)
        break
