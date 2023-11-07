import random 
import getpass

cadastro_realizado = False

def cadastrar_conta_corrente():
    global cadastro_realizado

    if cadastro_realizado:
        print("Você já realizou o cadastro uma vez. Não é permitido cadastrar mais de uma vez.")
        return 
    
    print("MACK BANK – CADASTRO DE CONTA")
    
    numero_conta = random.randint(1000, 9999)
    print("NÚMERO DA CONTA: ", numero_conta)
    
    nome_cliente = input("NOME DO CLIENTE: ")
    while not nome_cliente:
        print("Nome do cliente não pode estar em branco.")
        nome_cliente = input("NOME DO CLIENTE: ")
    
    telefone_cliente = input("TELEFONE.......: ")
    while not telefone_cliente:
        print("Telefone não pode estar em branco.")
        telefone_cliente = input("TELEFONE.......: ")
    
    email_cliente = input("EMAIL..........: ")
    while not email_cliente:
        print("Email não pode estar em branco.")
        email_cliente = input("EMAIL..........: ")
    
    saldo_inicial = float(input("SALDO INICIAL...:R$ "))
    while saldo_inicial < 1000:
        print("O saldo inicial deve ser maior ou igual a R$1000.")
        saldo_inicial = float(input("SALDO INICIAL...:R$ "))

    limite_credito = float(input("LIMITE DE CRÉDITO: R$ "))
    while limite_credito < 0:
        print("O limite de crédito não pode ser menor que 0.")
        limite_credito = float(input("LIMITE DE CRÉDITO: R$ "))

    senha = getpass.getpass("SENHA..........: ")
    while len(senha) != 6:
        print("A SENHA DEVE SER COMPOSTA POR 6 CARACTERES.")
        senha = getpass.getpass("SENHA..........: ")

    confirmacao_senha = getpass.getpass("REPITA A SENHA...: ")
    while confirmacao_senha != senha:
        print("AS SENHAS INSERIDAS NÃO SÃO IGUAIS.")
        confirmacao_senha = getpass.getpass("REPITA A SENHA...: ")
    
    cadastro_realizado = True

    input("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")




def depositar():
    print("Você escolheu a opção de depositar.")


def sacar():
    print("Você escolheu a opção de sacar.")


def consultar_saldo():
    print("Você escolheu a opção para consulta de saldo.")


def consultar_extrato():
    print("Você escolheu a opção para consulta de extrato.")


def finalizar():
    print("Você escolheu a opção para finalizar o programa.")


def imprimeEscolhas():
    print("MACK BANK - ESCOLHA UMA OPCÃO")
    print("   (1)   CADASTRAR CONTA CORRENTE")
    print("   (2)   DEPOSITAR")
    print("   (3)   SACAR")
    print("   (4)   CONSULTAR SALDO")
    print("   (5)   CONSULTAR EXTRATO")
    print("   (6)   FINALIZAR")
    
    opcao = int(input("SUA OPCÃO: "))
    
    while opcao < 1 or opcao > 6:
        opcao = int(input("OPCÃO INVÁLIDA, INSIRA UMA OPCAO VÁLIDA: "))
    
    if opcao == 1:
        cadastrar_conta_corrente()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        consultar_saldo()
    elif opcao == 5:
        consultar_extrato()
    elif opcao == 6:
        finalizar()


imprimeEscolhas()